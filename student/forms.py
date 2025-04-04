from django import forms

class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    birthday = forms.DateField()
    gender = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=15)
    url_picture = forms.URLField()
    mailticket = forms.CharField(max_length=100)
    phone_number_label= forms.CharField(max_length=100)
    classe = forms.CharField(max_length=100)
    ville = forms.CharField(max_length=100)
    pays = forms.CharField(max_length=100)
    rue = forms.CharField(max_length=100)
    pseudo = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
   
class SearchForm(forms.Form):
    query = forms.CharField(label='Rechercher', max_length=100)    