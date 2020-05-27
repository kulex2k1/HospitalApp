from django import forms
from django.forms import ModelForm
from .models import Patients, CaseHistory


class PatientsForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = '__all__'

class CaseHistoryForm(forms.ModelForm):
    class Meta:
        model = CaseHistory
        fields = '__all__'
        #exclude = ['create_date']
