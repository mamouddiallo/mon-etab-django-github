from django import forms

class SmtpForm(forms.Form):
    smtp_server = forms.CharField(label='Serveur SMTP', required=True)
    smtp_port = forms.IntegerField(label='Port SMTP', required=True)
    smtp_username = forms.CharField(label='Nom d\'utilisateur SMTP', required=True)
    smtp_password = forms.CharField(label='Mot de passe SMTP', widget=forms.PasswordInput, required=True)