# Generated by Django 4.2.13 on 2024-06-04 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_control_email_control_matricula_profesores_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calificaciones',
            name='control',
        ),
    ]
