# Generated by Django 3.0.6 on 2020-05-30 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0026_auto_20200530_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casehistory',
            name='entry_update',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='update_date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='schedule_date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='schedule_update',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
