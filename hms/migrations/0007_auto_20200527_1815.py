# Generated by Django 3.0.6 on 2020-05-27 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0006_auto_20200527_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casehistory',
            name='gender',
        ),
        migrations.AddField(
            model_name='casehistory',
            name='patient_name',
            field=models.CharField(max_length=150, null=True, verbose_name='Patient Name'),
        ),
        migrations.AlterField(
            model_name='casehistory',
            name='description',
            field=models.TextField(max_length=255, null=True, verbose_name='Description'),
        ),
    ]
