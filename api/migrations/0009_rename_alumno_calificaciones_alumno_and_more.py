# Generated by Django 4.2.13 on 2024-05-22 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_calificaciones_alumno_calificaciones_profesor_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calificaciones',
            old_name='Alumno',
            new_name='alumno',
        ),
        migrations.RenameField(
            model_name='calificaciones',
            old_name='Control',
            new_name='control',
        ),
        migrations.RenameField(
            model_name='calificaciones',
            old_name='Profesor',
            new_name='profesor',
        ),
    ]
