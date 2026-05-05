from django.urls import path
from rest_framework.routers import DefaultRouter

from users.views import SMSVerificationViewSet, CustomTokenRefreshView


router = DefaultRouter()
router.register('auth/phone', SMSVerificationViewSet, basename='phone-auth')

urlpatterns = router.urls + [
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]