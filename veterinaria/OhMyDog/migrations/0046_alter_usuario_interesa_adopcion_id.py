# Generated by Django 4.2.1 on 2023-06-26 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OhMyDog', '0045_rename_adopcion_usuario_interesa_adopcion_adopcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario_interesa_adopcion',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
