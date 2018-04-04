from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    first_name = forms.CharField(label="FirstName")
    username = forms.CharField(label="UserName")
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(label="Email")

    class Meta:
        model = User
        fields = ['first_name', 'username', 'password', 'email']