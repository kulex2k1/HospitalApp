from django.shortcuts import render, redirect, reverse
from .forms import PatientsForm, CaseHistoryForm, AddCaseForm, ScheduleForm
from .models import Patients, CaseHistory, Payments, Schedule
from .filter import PatientsFilter, ScheduleFilter



# Create your views here.
def test(request): 

    return render(request, 'hms/viewHistory2.html')


def home(request): 
    patients = Patients.objects.all()
    context = {'patients': patients} 
    return render(request, 'tablewithcard.html', context)


def index(request):
    return render(request, 'index.html')


def addPatient(request):
    form = PatientsForm()
    if request.method == 'POST':
       form = PatientsForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect ('home')
    form = PatientsForm()
    context = {'form':form}
    return render(request, 'hms/addPatient.html', context)


""" def patientList(request):
    patients =  Patients.objects.all().order_by('create_date')
    myFilter = PatientsFilter(request.GET, queryset = patients)
    patients = myFilter.qs
    context = {'patients': patients, 'myFilter': myFilter}
    return render(request, 'tableonly.html', context) """


def patientList(request, pk):
    schedules =  Schedule.objects.filter(id=pk)
    myFilter = ScheduleFilter(request.GET, queryset = schedules)
    patients = myFilter.qs
    context = {'schedules': schedules, 'myFilter': myFilter}
    return render(request, 'tableonly.html', context)


def viewPatient(request, pk):
    patient = Patients.objects.get(id=pk)
    context = {'patient': patient}
    return render(request, 'hms/viewPatient.html', context)


def editPatient(request, pk):
    patient = Patients.objects.get(id=pk)
    form = PatientsForm(instance = patient)
    if request.method == 'POST':
        form = PatientsForm(request.POST, instance = patient)
        if form.is_valid():
           form.save()
           return redirect ('patientList')
    context = {'form':form}
    return render(request, 'hms/editPatient.html', context)


def caseHistory(request):
    form = CaseHistoryForm()
    if request.method == 'POST':
        form = CaseHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')   
    form = CaseHistoryForm()
    context = {'form':form}
    return render(request, 'hms/caseHistory.html', context)

def Payments(request):
    return render(request, 'hms/payment.html')


def queue(request):
    patients =  Patients.objects.all().order_by('create_date')

    myFilter = PatientsFilter(request.GET, queryset = patients)
    patients = myFilter.qs
    context = {'patients': patients, 'myFilter': myFilter}
    return render(request, 'tableandcard.html', context)


def AddCase(request, pk):
    cases = Patients.objects.get(id=pk)
    form = CaseHistoryForm()
    if request.method == 'POST':
        form = CaseHistoryForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patientList')   
    form = CaseHistoryForm()
    context = {'cases': cases, 'form': form}
    return render(request, 'hms/addCase.html', context)


def viewCaseHistory(request, pk):
    history = CaseHistory.objects.filter(patient_name_id=pk)
    pat = Patients.objects.get(id=pk)
    context = {'history': history, 'pat': pat}
  
    return render(request, 'hms/viewHistory.html', context)



def addSchedule(request, pk):
    patients = Patients.objects.get(id=pk)
    form = ScheduleForm()
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect ('home')
    context = {'form':form, 'patients':patients } 
    return render(request, 'hms/schedule.html', context)