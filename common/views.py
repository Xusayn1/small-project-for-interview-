from rest_framework.views import APIView
from rest_framework.response import Response
from access.utils import check_permission


class ProductView(APIView):
    def get(self, request):
        if not request.user:
            return Response({"error": "Unauthorized"}, status=401)

        if not check_permission(request.user, "product", "read"):
            return Response({"error": "Forbidden"}, status=403)

        return Response({"data": ["product1", "product2"]})
    