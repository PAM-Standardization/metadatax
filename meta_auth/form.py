from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import EmailField, BooleanField, CharField, EmailInput, PasswordInput

from .models import User


class SignupForm(UserCreationForm):
    email = EmailField(
        max_length=200,
        widget=EmailInput(attrs={"autocomplete": "on"})
    )
    accept_mailing = BooleanField(
        label="I want to receive updates on Metadatax project",
        label_suffix="",
        required=False
    )
    institution = CharField(required=False)

    class Meta:
        model = User
        fields = ('email', 'institution', 'password1', 'password2', 'accept_mailing')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
