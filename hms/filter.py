import django_filters
from django_filters import CharFilter
from .models import Patients, Schedule


class PatientsFilter(django_filters. FilterSet):
    fullName = CharFilter(field_name = 'fullName', lookup_expr = 'icontains')
    class Meta:
        model = Patients
        fields = ['fullName']


class ScheduleFilter(django_filters. FilterSet):
    fullName = CharFilter(field_name = 'patient_name', lookup_expr = 'icontains')
    class Meta:
        model = Schedule
        fields = ['patient_name']