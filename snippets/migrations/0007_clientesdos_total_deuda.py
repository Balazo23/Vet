# Generated by Django 5.1.7 on 2025-04-04 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0006_remove_mascotas_estado_mascota_facturas_monto_pagado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientesdos',
            name='total_deuda',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
