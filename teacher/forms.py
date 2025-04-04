from django import forms

class TeacherForm(forms.Form):
    gender = forms.CharField(max_length=100)
    birthday = forms.DateField(required=False)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=15)
    url_picture = forms.URLField(required=False)
    available = forms.CharField(required=False)
    specially = forms.CharField(max_length=100)
    ville = forms.CharField(max_length=100)
    pays = forms.CharField(max_length=100)
    rue = forms.CharField(max_length=100)
    pseudo= forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)