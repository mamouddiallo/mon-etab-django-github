from django import forms

class UserForm(forms.Form):
    pseudo = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)