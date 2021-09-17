from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    username = forms.CharField(max_length=30)
    password = forms.PasswordInput()
    password1 = forms.CharField(
    label=("Password"),
    strip=False,
    widget=forms.PasswordInput)
    
    password2 = forms.CharField(
    label=("Confirm Password"),
    strip=False,
    widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        




class loginForm(forms.ModelForm):
    username = forms.CharField(max_length=30)
    password1 = forms.CharField(
    label=("Password"),
    strip=False,
    widget=forms.PasswordInput)
    

    class Meta:
        model = User
        fields = ('username',  'password1' )