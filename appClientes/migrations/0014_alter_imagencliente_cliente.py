# Generated by Django 5.0.6 on 2024-06-17 23:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appClientes', '0013_alter_imagencliente_cliente_alter_resenya_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagencliente',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appClientes.cliente'),
        ),
    ]