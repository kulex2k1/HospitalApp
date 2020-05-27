import django_filters
from django_filters import CharFilter
from .models import Patients


class PatientsFilter(django_filters. FilterSet):
    fullName = CharFilter(field_name = 'fullName', lookup_expr = 'icontains')
    class Meta:
        model = Patients
        fields = ['fullName']
   