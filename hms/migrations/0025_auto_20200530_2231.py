# Generated by Django 3.0.6 on 2020-05-30 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0024_auto_20200530_2230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='scheduled_name',
            new_name='patient_name',
        ),
    ]
