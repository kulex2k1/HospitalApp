from django.db import models

# Create your models here.
class Patients(models.Model):
    fullName = models.CharField('Full Name', max_length=150, null = True)
    
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    
    ]
    gender = models.CharField(
        max_length=10,
        choices=gender_choices,
        default= "AB+",
    )


    blood_group_choices = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]
    blood_group = models.CharField(
        max_length=10,
        choices=blood_group_choices,
        default= "---",
    )
    birth_date = models.DateField('Date of Birth', null = True)
    phone = models.CharField('Phone Number', max_length=150, null = True)
    address = models.CharField('Address', max_length=150, null = True)
    patient_email = models.EmailField('Email', max_length=150, null = True)

    status_choices = [
        ('------', '-------'),
        ('Active', 'Active'),
        ('In-Active', 'In-Active'),
    
    ]
    status = models.CharField(
        max_length=20,
        choices=status_choices,
        default= "---",
    )

    create_date = models.DateField(auto_now_add=True, null = True)
    update_date = models.DateTimeField(auto_now=True,  null = True)
    # image = models.ImageField(upload_to= 'images', height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
        return self.fullName


class CaseHistory(models.Model):
    entry_date = models.DateField(auto_now_add=True, null = True)
    patient_name = models.ForeignKey('Patients', related_name='patient_names', on_delete=models.CASCADE)
    patient = models.CharField('Patients Name', max_length=150, null = True)
    description = models.TextField( null = True)
    entry_update = models.DateTimeField(auto_now=True,  null = True)


    case_status_choices = [
        ('------', '-------'),
        ('Diagnosed', 'Diagnosed'),
        ('Not Diagnosed', 'Not Diagnosed'),
    ]
    case_status = models.CharField(
        max_length=20,
        choices=case_status_choices,
        default= "",
    )
    # image = models.ImageField(upload_to= 'images', height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
        return self.description



class Payments(models.Model):
    invoice = models.CharField('Invoice', max_length=150, null = True)
    patient_name = models.CharField('Patients Name', max_length=150, null = True)
    service = models.CharField('Service', max_length=150, null = True)
    Service_Cost = models.CharField('Service Cost', max_length=150, null = True)
    amount_recieved = models.CharField('Amount Recieved', max_length=150, null = True)
    # image = models.ImageField(upload_to= 'images', height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.invoice 

class Deposit(models.Model):
    service_invoice = models.ForeignKey("Payments", verbose_name="service_invoice", on_delete=models.CASCADE)
    deposit_amount = models.CharField('Amount Deposited', max_length=150, null = True)
    # image = models.ImageField(upload_to= 'images', height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.deposit_amount 


class Schedule(models.Model):
    patient_name = models.CharField('Patients', max_length=150, null = True)
    schedule_date = models.DateTimeField(auto_now=True,  null = True)
    temperature  = models.CharField('Temprature', max_length=150, null = True)
    blood_pressure = models.CharField('Blood Pressure', max_length=150, null = True)
    schedule_update = models.DateTimeField(auto_now=True,  null = True)
    def __str__(self):
        return self.temperature  


  

