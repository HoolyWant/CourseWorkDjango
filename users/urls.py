from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, VerifyView, VerifySuccess, VerifyError, ChangePassword, ErrorPasswordChange

app_name = UsersConfig.name

urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
    path('verify/', VerifyView.as_view(), name='verify'),
    path('verify_success/', VerifySuccess.as_view(), name='verify_success'),
    path('verify_error/', VerifyError.as_view(), name='verify_error'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change_password/', ChangePassword.as_view(), name='change_password'),
    path('error_password_change/', ErrorPasswordChange.as_view(), name='error_password_change')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)