# Generated by Django 4.2.1 on 2023-06-01 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OhMyDog', '0023_atencion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atencion',
            name='perro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OhMyDog.perro'),
        ),
    ]
