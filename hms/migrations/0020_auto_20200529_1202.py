# Generated by Django 3.0.6 on 2020-05-29 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0019_remove_casehistory_case_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='casehistory',
            name='choice_status',
            field=models.CharField(choices=[('Diagnosed', 'Diagnosed'), ('Not Diagnosed', 'Not Diagnosed')], default='Active', max_length=20),
        ),
        migrations.AlterField(
            model_name='patients',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('In-Active', 'In-Active')], default='Active', max_length=20),
        ),
    ]
