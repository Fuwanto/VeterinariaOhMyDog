# Generated by Django 4.2.1 on 2023-05-19 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OhMyDog', '0017_alter_usuario_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cliente',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='OhMyDog.cliente'),
        ),
    ]
