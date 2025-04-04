from django import forms

class AbsenceForm(forms.Form):
    absence_date = forms.DateField()
    absence_number = forms.IntegerField()
