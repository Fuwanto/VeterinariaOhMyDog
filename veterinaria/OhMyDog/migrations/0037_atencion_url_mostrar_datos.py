# Generated by Django 4.2.1 on 2023-06-12 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OhMyDog', '0036_vacunacion_fabricante_vacunacion_num_lote_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='atencion',
            name='url_mostrar_datos',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
