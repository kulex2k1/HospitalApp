# Generated by Django 3.0.6 on 2020-05-29 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0020_auto_20200529_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casehistory',
            name='choice_status',
        ),
        migrations.AddField(
            model_name='casehistory',
            name='case_status',
            field=models.CharField(choices=[('Diagnosed', 'Diagnosed'), ('Not Diagnosed', 'Not Diagnosed')], default='----', max_length=20),
        ),
        migrations.AlterField(
            model_name='patients',
            name='blood_group',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], default='---', max_length=10),
        ),
        migrations.AlterField(
            model_name='patients',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('In-Active', 'In-Active')], default='---', max_length=20),
        ),
    ]