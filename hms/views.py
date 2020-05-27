from django.shortcuts import render, redirect
from .forms import PatientsForm, CaseHistoryForm
from .models import Patients, CaseHistory
from .filter import PatientsFilter



# Create your views here.
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


def patientList(request):
    patients = Patients.objects.all()
    myFilter = PatientsFilter(request.GET, queryset = patients)
    patients = myFilter.qs
    context = {'patients': patients, 'myFilter': myFilter}
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

""" def viewCaseHistory(request, pk):
    history = CaseHistory.objects.get(id=pk)
    form = CaseHistoryForm(instance = history)
    if request.method == 'POST':
        form = CaseHistoryForm(request.POST, instance = history)
        if form.is_valid():
            form.save()
            return redirect('patientList')   
    context = {'form':form}
    return render(request, 'hms/caseHistory.html', context) """

def viewCaseHistory(request, pk):
    history = CaseHistory.objects.get(id=pk)

    context = {'history': history}
    return render(request, 'hms/viewHistory.html', context)