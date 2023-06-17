# Generated by Django 4.2.1 on 2023-06-16 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OhMyDog', '0040_busqueda'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paseador',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('latitud', models.TextField()),
                ('longitud', models.TextField()),
                ('franja_horaria', models.CharField(max_length=255)),
            ],
        ),
    ]
