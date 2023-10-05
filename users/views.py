from secrets import token_hex

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/user_form.html'

    def form_valid(self, form):
        send_mail('Email verify',
                  f'Write this token {form.instance.verify_token}',
                  'sir.saltickow@yandex.ru',
                  [form.instance.email, ])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('users:verify')


class VerifyView(View):
    template_name = 'users/verify.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        verification_code = request.POST.get('verification_code')
        User = get_user_model()
        try:
            user = User.objects.get(verify_token=verification_code)
            if user.is_active is False:
                user.is_active = True
                user.save()
                return redirect('users:verify_success')
        except User.DoesNotExist:
            pass


class VerifyError(View):
    template_name = 'users/verify_error.html'

    def get(self, request):
        return render(request, self.template_name)


class VerifySuccess(View):
    template_name = 'users/verify_success.html'

    def get(self, request):
        return render(request, self.template_name)


class ChangePassword(View):

    template_name = 'users/change_password.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST.get('email')
        User = get_user_model()
        try:
            user = User.objects.get(email=email)
            new_password = token_hex(6)
            user.set_password(new_password)
            send_mail('Change password',
                      f'New password: {new_password}',
                      EMAIL_HOST_USER,
                      [email, ])
            user.save()
            return redirect('users:login')
        except User.DoesNotExist:
            pass
        return redirect('users:error_password_change')


class ErrorPasswordChange(View):
    template_name = 'users/error_password_change.html'

    def get(self, request):
        return render(request, self.template_name)
