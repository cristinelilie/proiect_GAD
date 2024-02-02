from django import forms
from .models import Products
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['product', 'description']
        widgets = {
            'product': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Product',
            }),
            'description': forms.Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; height: 100px;',
                'placeholder': 'Description',
            })
        }


# Create User
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Authenticate user
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput(attrs={
        'class': "form-control",
        'style': 'max-width: 300px; margin: auto;',
        'placeholder': 'Username',
    }))
    password = forms.CharField(widget=PasswordInput(attrs={
        'class': "form-control",
        'style': 'max-width: 300px; margin: auto;',
        'placeholder': 'Password',
    }))
