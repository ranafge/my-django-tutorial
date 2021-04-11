from django.contrib.auth.views import PasswordResetConfirmView
from django.shortcuts import render
from django.urls import reverse_lazy

from . import forms
# Create your views here.
class UserAccountResetPasswordView(PasswordResetConfirmView):
    template_name = 'password_related/reset_password.html'
    form_class = forms.UserAccountPasswordResetForm
    success_url = reverse_lazy('user_account:login')
    extra_context = {
        'template_name': 'password_related/reset_password_failed.html'
    }