# Generated by Django 5.0.7 on 2024-08-08 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management', '0004_alter_employee_options_employee_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='password',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
