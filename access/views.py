from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AccessRule


class AccessRuleView(APIView):
    def get(self, request):
        if request.user.role.name != 'admin':
            return Response({"error": "Forbidden"}, status=403)

        rules = AccessRule.objects.all().values()
        return Response(list(rules))

    def post(self, request):
        if request.user.role.name != 'admin':
            return Response({"error": "Forbidden"}, status=403)

        rule = AccessRule.objects.create(**request.data)
        return Response({"message": "Rule created"})