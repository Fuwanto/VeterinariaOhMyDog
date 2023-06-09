# Generated by Django 4.2.1 on 2023-05-31 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OhMyDog', '0022_perro_habilitado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atencion',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('observacion', models.TextField(null=True)),
                ('perro', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='OhMyDog.perro')),
                ('tipo_atencion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OhMyDog.tipodeatencion')),
            ],
        ),
    ]
