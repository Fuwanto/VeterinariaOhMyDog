# Generated by Django 4.2.1 on 2023-06-09 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OhMyDog', '0032_turno_perro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perro',
            name='dueño',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perros', to='OhMyDog.cliente'),
        ),
    ]
