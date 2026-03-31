from django.urls import path
from .views import AccessRuleView

urlpatterns = [
    path('access-rules/', AccessRuleView.as_view()),
]