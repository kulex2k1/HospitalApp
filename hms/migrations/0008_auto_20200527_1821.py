# Generated by Django 3.0.6 on 2020-05-27 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0007_auto_20200527_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casehistory',
            name='description',
            field=models.CharField(max_length=255, null=True, verbose_name='Description'),
        ),
    ]
