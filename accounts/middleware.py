import jwt
from django.http import JsonResponse
from .models import User, BlacklistedToken


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        auth_header = request.headers.get('Authorization')

        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]

            # 🔒 blacklist check
            if BlacklistedToken.objects.filter(token=token).exists():
                return JsonResponse({"error": "Token expired"}, status=401)

            try:
                payload = jwt.decode(token, "SECRET_KEY", algorithms=['HS256'])
                user = User.objects.get(id=payload['user_id'])

                if user.is_active:
                    request.user = user

            except Exception:
                return JsonResponse({"error": "Invalid token"}, status=401)

        # ❗ header yo‘q bo‘lsa — shunchaki davom etadi
        return self.get_response(request)