# Generated by Django 4.2.1 on 2023-06-19 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OhMyDog', '0042_paseadorcuidador_delete_paseador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turno',
            name='notas',
        ),
    ]
