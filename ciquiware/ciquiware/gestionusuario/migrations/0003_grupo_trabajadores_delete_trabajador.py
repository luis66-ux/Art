# Generated by Django 5.0.6 on 2024-06-13 01:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionusuario', '0002_alter_customuser_cargo_division_area_grupo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='trabajadores',
            field=models.ManyToManyField(limit_choices_to={'cargo': 'TRABAJADOR'}, related_name='grupos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Trabajador',
        ),
    ]
