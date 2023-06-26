# Generated by Django 4.2.1 on 2023-06-26 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OhMyDog', '0047_usuario_tiene_informacion_busqueda'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioInteresaAdopcion',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('adopcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OhMyDog.adopcion')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OhMyDog.cliente')),
            ],
        ),
        migrations.RenameModel(
            old_name='Usuario_tiene_informacion_busqueda',
            new_name='UsuarioTieneInformacionBusqueda',
        ),
        migrations.DeleteModel(
            name='Usuario_interesa_adopcion',
        ),
    ]
