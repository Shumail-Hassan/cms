# Generated by Django 5.0.7 on 2024-08-08 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management', '0003_alter_employee_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'permissions': (('is_admin', 'Is Admin'), ('is_employee', 'Is Employee'))},
        ),
        migrations.AddField(
            model_name='employee',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
