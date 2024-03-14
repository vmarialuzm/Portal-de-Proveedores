# Generated by Django 5.0.3 on 2024-03-14 15:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitudCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.proveedores')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleSolicitudCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=100)),
                ('enlace_producto', models.URLField()),
                ('cantidad', models.IntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio_total', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('solicitud_compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitud_compra.solicitudcompra')),
            ],
        ),
    ]
