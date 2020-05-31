from django.contrib import admin
from .models import Patients, CaseHistory, Schedule
# Register your models here.
admin.site.register(Patients)
admin.site.register(CaseHistory)
admin.site.register(Schedule)
