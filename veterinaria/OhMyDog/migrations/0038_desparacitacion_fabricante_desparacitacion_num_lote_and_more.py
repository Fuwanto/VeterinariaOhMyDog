# Generated by Django 4.2.1 on 2023-06-12 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OhMyDog', '0037_atencion_url_mostrar_datos'),
    ]

    operations = [
        migrations.AddField(
            model_name='desparacitacion',
            name='fabricante',
            field=models.CharField(default='asd', max_length=50),
        ),
        migrations.AddField(
            model_name='desparacitacion',
            name='num_lote',
            field=models.CharField(default='asd', max_length=50),
        ),
        migrations.AddField(
            model_name='desparacitacion',
            name='num_serie',
            field=models.CharField(default='asd', max_length=50),
        ),
    ]
