# Generated by Django 3.1.2 on 2020-12-08 14:20

import almacen.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0002_auto_20201125_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.CharField(default=almacen.models.generate_uuid, editable=False, max_length=40, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Posicion',
            fields=[
                ('id', models.CharField(default=almacen.models.generate_uuid, editable=False, max_length=40, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProductoTipo',
            fields=[
                ('id', models.CharField(default=almacen.models.generate_uuid, editable=False, max_length=40, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='almacen',
            name='id',
            field=models.CharField(default=almacen.models.generate_uuid, editable=False, max_length=40, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='almacen',
            name='marca',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='marca', to='almacen.marca'),
        ),
        migrations.AlterField(
            model_name='almacen',
            name='tipo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='producto', to='almacen.productotipo'),
        ),
        migrations.AlterField(
            model_name='almacen',
            name='ubicacion',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ubicacion', to='almacen.posicion'),
        ),
    ]