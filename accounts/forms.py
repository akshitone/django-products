from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

not_allowed_username = ['']


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        user = User.objects.filter(username__iexact=username)
        if username in not_allowed_username:
            raise forms.ValidationError("This username is already exists!")
        if user.exists():
            raise forms.ValidationError("This username is already exists!")

        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        user = User.objects.filter(email__iexact=email)
        if user.exists():
            raise forms.ValidationError("This email is already exists!")

        return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    # you can add CSS classes using PasswordInput(attrs={'class':...})

    # this function run after clean_... and it has additional features
    # def clean(self):
    #     username = self.cleaned_data.get("username")
    #     password = self.cleaned_data.get("password")

    def clean_username(self):
        username = self.cleaned_data.get("username")
        # AkSHiT == akshit ---> __iexact
        user = User.objects.filter(username__iexact=username)
        if not user.exists():
            raise forms.ValidationError("Invalid user!")

        return username
