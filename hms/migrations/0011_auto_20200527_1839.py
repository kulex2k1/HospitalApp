# Generated by Django 3.0.6 on 2020-05-27 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0010_remove_casehistory_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casehistory',
            name='create_date',
        ),
        migrations.RemoveField(
            model_name='casehistory',
            name='update_date',
        ),
        migrations.AddField(
            model_name='casehistory',
            name='description',
            field=models.TextField(default='Enter'),
        ),
    ]
