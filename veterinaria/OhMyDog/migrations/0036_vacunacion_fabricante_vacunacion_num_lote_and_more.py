# Generated by Django 4.2.1 on 2023-06-11 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OhMyDog', '0035_merge_20230611_0156'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacunacion',
            name='fabricante',
            field=models.CharField(default='asd', max_length=50),
        ),
        migrations.AddField(
            model_name='vacunacion',
            name='num_lote',
            field=models.CharField(default='asd', max_length=50),
        ),
        migrations.AddField(
            model_name='vacunacion',
            name='num_serie',
            field=models.CharField(default='asd', max_length=50),
        ),
        migrations.AlterField(
            model_name='vacunacion',
            name='dosis',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='vacunacion',
            name='vacuna',
            field=models.CharField(choices=[('Antiviral', 'Antiviral'), ('Antirrabica', 'Antirrabica')], max_length=14),
        ),
    ]