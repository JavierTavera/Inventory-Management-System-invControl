# Generated by Django 4.2.7 on 2023-12-19 20:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0006_tipoproducto_referencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('codigoQR', models.CharField(blank=True, max_length=200, null=True)),
                ('lote', models.CharField(max_length=100)),
                ('fecha_vencimiento', models.CharField(blank=True, max_length=50, null=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('IdBodega', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.bodega')),
                ('IdEstado_producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.estadoproducto')),
            ],
        ),
        migrations.AddField(
            model_name='referencia',
            name='IdProveedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.proveedor'),
        ),
        migrations.CreateModel(
            name='Transacciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otro_estado', models.CharField(blank=True, max_length=80, null=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('IdBodega', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.bodega')),
                ('IdEstado_producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.estadoproducto')),
                ('IdProducto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.producto')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='IdReferencia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.referencia'),
        ),
        migrations.AddField(
            model_name='producto',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
