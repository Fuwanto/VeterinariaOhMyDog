# Generated by Django 4.2.1 on 2023-07-06 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OhMyDog', '0055_remove_transaccion_transaccion_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaccion',
            name='id',
        ),
        migrations.AddField(
            model_name='transaccion',
            name='transaccion_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
