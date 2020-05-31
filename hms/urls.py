from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('addPatient/', views.addPatient, name='addPatient'),
    path('patientList/<str:pk>/', views.patientList, name='patientList'),
    path('editPatient/<str:pk>/', views.editPatient, name='edit'),
    path('viewPatient/<str:pk>/', views.viewPatient, name='view'),
    path('caseHistory', views.caseHistory, name='case'),
    path('viewHistory/<str:pk>/', views.viewCaseHistory, name='viewHistory'),
    path('payments', views.Payments, name='payments'),
    path('addCase/<str:pk>/', views.AddCase, name='addCase'),
    path('queue', views.queue, name='queue'),
    path('schedule/<str:pk>/', views.addSchedule, name='schedule'),
]
