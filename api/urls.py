from django.urls import path, include
from dj_rest_auth.views import PasswordResetConfirmView


urlpatterns = [
    path('api/', include('rest_framework.urls')),
    path('api/auth/password/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),
]
