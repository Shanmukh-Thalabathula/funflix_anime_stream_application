from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'auth-input', 'placeholder': 'Enter First Name'}),
        label='First Name'
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'auth-input', 'placeholder': 'Enter Last Name'}),
        label='Last Name'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'auth-input', 'placeholder': 'Enter Gmail'}),
        label='Gmail'
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'auth-input', 'placeholder': 'Enter Username'}),
        label='Username'
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'auth-input', 'placeholder': 'Enter Password'}),
        label='Password'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'auth-input', 'placeholder': 'Confirm Password'}),
        label='Confirm Password'
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'auth-input', 'placeholder': 'Enter Username'}),
        label='Username'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'auth-input', 'placeholder': 'Enter Password'}),
        label='Password'
    )

    class Meta:
        model = User
        fields = ['username', 'password']
