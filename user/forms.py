from django import forms
from django.contrib.auth.forms import AuthenticationForm
from user.models.user import UserModels



class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='Pseudo',
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Votre pseudo',
            'autofocus': True
        })
    )
    
    password = forms.CharField(
        label='Mot de passe',
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Votre mot de passe'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        pseudo = cleaned_data.get('username')
        password = cleaned_data.get('password')
        
        if pseudo and password:
            user = UserModels.objects.filter(pseudo=pseudo).first()
            
            if user is None:
                raise forms.ValidationError("Ce pseudo n'existe pas")
            
            if not user.check_password(password):
                raise forms.ValidationError("Mot de passe incorrect")
        
        return cleaned_data

