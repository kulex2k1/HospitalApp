# Generated by Django 3.0.6 on 2020-05-27 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0012_auto_20200527_1842'),
    ]

    operations = [
        migrations.RenameField(
            model_name='casehistory',
            old_name='create_date',
            new_name='entry_date',
        ),
        migrations.RenameField(
            model_name='casehistory',
            old_name='update_date',
            new_name='entry_update',
        ),
        migrations.AlterField(
            model_name='casehistory',
            name='description',
            field=models.TextField(null=True),
        ),
    ]