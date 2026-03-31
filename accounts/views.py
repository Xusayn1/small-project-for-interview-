import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .utils import generate_token
from .models import BlacklistedToken

logger = logging.getLogger(__name__)

class ProfileView(APIView):
    def get(self, request):
        if not request.user:
            return Response({"error": "Unauthorized"}, status=401)

        return Response({
            "email": request.user.email,
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
        })

    def put(self, request):
        user = request.user

        if not user:
            return Response({"error": "Unauthorized"}, status=401)

        user.first_name = request.data.get('first_name', user.first_name)
        user.last_name = request.data.get('last_name', user.last_name)
        user.save()

        return Response({"message": "Updated"})
    
class DeleteAccountView(APIView):
    def delete(self, request):
        user = request.user

        if not user:
            return Response({"error": "Unauthorized"}, status=401)

        user.is_active = False
        user.save()

        return Response({"message": "Account deactivated"})


class LogoutView(APIView):
    def post(self, request):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return Response({"error": "No token"}, status=400)

        token = auth_header.split(' ')[1]

        BlacklistedToken.objects.create(token=token)

        return Response({"message": "Logged out"})


class RegisterView(APIView):
    def post(self, request):
        data = request.data

        try:
            email = data["email"]
            password = data["password"]
        except KeyError:
            return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            email=email,
            password=password,
            first_name=data.get('first_name', ''),
            last_name=data.get('last_name', '')
        )

        logger.debug(f"User created: {user.email}")

        return Response({"message": "User registered"}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        data = request.data

        try:
            email = data["email"]
            password = data["password"]
        except KeyError:
            return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            logger.warning("Login failed: user not found")
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.check_password(password):
            logger.warning("Login failed: wrong password")
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.is_active:
            return Response({"error": "User is inactive"}, status=status.HTTP_403_FORBIDDEN)

        token = generate_token(user.id)

        return Response({"token": token})
