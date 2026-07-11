from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'class': 'password-field', 
                'placeholder': 'Пароль'                
            }
        )
    )

    password_confirm = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'password-field',
                'placeholder': 'Подтвердите пароль'
            }
        )
    )


    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'username-field',
                    'placeholder': 'Имя пользователя'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'email-field',
                    'placeholder': 'E-mail'
                }
            )
        }


class UserLoginForm(AuthenticationForm):
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'class': 'password-field', 
                'placeholder': 'Пароль'                
            }
        )
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'username-field',
                'placeholder': 'Имя пользователя'
            }
        )
    )