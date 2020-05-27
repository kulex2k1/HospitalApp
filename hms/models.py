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
        default= "AB+",
    )
    birth_date = models.DateField('Date of Birth', null = True)
    phone = models.CharField('Phone Number', max_length=150, null = True)
    address = models.CharField('Address', max_length=150, null = True)
    patient_email = models.EmailField('Email', max_length=150, null = True)
    status = models.BooleanField(default= False, null = True)
    create_date = models.DateField(auto_now_add=True, null = True)
    update_date = models.DateTimeField(auto_now=True,  null = True)
    # image = models.ImageField(upload_to= 'images', height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.fullName


class CaseHistory(models.Model):
    entry_date = models.DateField(auto_now_add=True, null = True)
    patient_name = models.ForeignKey('Patients', verbose_name='', on_delete=models.CASCADE)
    description = models.TextField( null = True)
    entry_update = models.DateTimeField(auto_now=True,  null = True)
    # image = models.ImageField(upload_to= 'images', height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.description