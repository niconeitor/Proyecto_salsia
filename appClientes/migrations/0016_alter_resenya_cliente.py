# Generated by Django 5.0.6 on 2024-06-21 16:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appClientes', '0015_alter_resenya_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resenya',
            name='cliente',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appClientes.cliente'),
        ),
    ]