# Generated by Django 4.2.1 on 2023-05-10 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OhMyDog', '0005_alter_cliente_email_alter_cliente_nombre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='primerInicio',
            field=models.BooleanField(default=True),
        ),
    ]