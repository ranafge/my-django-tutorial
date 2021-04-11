from crispy_forms.bootstrap import AppendedText
from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import SetPasswordForm, ValidationError
from django.utils.translation import ugettext_lazy as _
import re
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'placeholder': 'New Password', 'class': 'password1'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Password', 'class': 'password2'}),
    )

class UserAccountPasswordResetForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'toggle-password-type',
                'placeholder': 'New Password'
            }),
    )
    new_password2 = forms.CharField(
        label=_("Confirm new password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm New Password'
            }),
    )

    class Meta:
        fields = ['new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field(AppendedText('new_password1',
                  '<i onclick="passwordTypeToggle()" class="fa fa-eye"></i>')),
            'new_password2',
        )

    def clean_new_password1(self):
        new_password1 = self.cleaned_data.get("new_password1")
        if not re.search(
                "^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d@!#$%&*()_+-= ]{8,}$",
                new_password1
        ):
            raise ValidationError(
                'Password should have 8 to 15 characters which contain only characters, numeric digits, underscore and first character must be a letter', code='signup'
            )
        return new_password1