# Generated by Django 4.2.5 on 2023-12-22 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0003_alter_cliente_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(max_length=50, verbose_name='La direccion'),
        ),
    ]
