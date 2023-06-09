# Generated by Django 4.2.1 on 2023-05-10 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OhMyDog', '0006_cliente_primerinicio'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDeUsuario',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='contraseña',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='primerInicio',
        ),
        migrations.AddField(
            model_name='cliente',
            name='habilitado',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('usuario', models.EmailField(max_length=255)),
                ('contraseña', models.CharField(max_length=255)),
                ('habilitado', models.BooleanField(default=True)),
                ('primer_inicio', models.BooleanField(default=True)),
                ('cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OhMyDog.cliente')),
                ('tipo_usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OhMyDog.tipodeusuario')),
            ],
        ),
    ]
