# Generated by Django 4.2.1 on 2023-05-19 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OhMyDog', '0012_alter_perro_dueño'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perro',
            name='dueño',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OhMyDog.cliente'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cliente_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='OhMyDog.cliente'),
        ),
    ]
