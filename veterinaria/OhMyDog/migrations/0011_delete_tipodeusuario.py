# Generated by Django 4.2.1 on 2023-05-19 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OhMyDog', '0010_alter_usuario_mail_alter_usuario_password'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TipoDeUsuario',
        ),
    ]
