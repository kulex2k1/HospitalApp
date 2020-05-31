from django import forms
from django.forms import ModelForm
from .models import Patients, CaseHistory, Payments, Schedule


class PatientsForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = '__all__'

class CaseHistoryForm(forms.ModelForm):
    class Meta:
        model = CaseHistory
        fields = '__all__'
        exclude = ['patient']


class AddCaseForm(forms.ModelForm):
    class Meta:
        model = CaseHistory
        fields = '__all__'
        exclude = ['patient_name','patient' ]


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__' 
        exclude = ['patient_name']