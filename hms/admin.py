from django.contrib import admin
from .models import Patients, CaseHistory
# Register your models here.
admin.site.register(Patients)
admin.site.register(CaseHistory)