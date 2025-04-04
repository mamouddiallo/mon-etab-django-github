from django import forms

class SchoolForm(forms.Form):
    name = forms.CharField(max_length=100)
    url_logo = forms.URLField(required=False)