# Generated by Django 4.2.1 on 2023-05-30 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OhMyDog', '0021_rename_cliente_id_turno_cliente_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='perro',
            name='habilitado',
            field=models.BooleanField(default=True),
        ),
    ]