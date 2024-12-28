from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter username'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter email'})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'})
    )

class LoginForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter email'})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'})
    )