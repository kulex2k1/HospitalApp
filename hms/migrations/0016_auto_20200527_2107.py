# Generated by Django 3.0.6 on 2020-05-27 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0015_auto_20200527_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casehistory',
            name='entry_update',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='update_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
