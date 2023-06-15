# Generated by Django 4.2.1 on 2023-06-15 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OhMyDog', '0039_merge_20230612_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Busqueda',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField(null=True)),
                ('zona', models.TextField()),
                ('encontrado', models.BooleanField(default=False)),
                ('foto', models.ImageField(upload_to='fotos/')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OhMyDog.cliente')),
            ],
        ),
    ]
