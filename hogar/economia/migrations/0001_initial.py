# Generated by Django 3.1.5 on 2021-02-17 02:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import economia.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_OP',
            fields=[
                ('id', models.CharField(default=economia.models.generate_uuid, editable=False, max_length=40, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=20)),
                ('des', models.CharField(max_length=100)),
                ('tipo', models.CharField(blank=True, choices=[('Entrada', 'Entrada'), ('Salida', 'Salida')], max_length=20, null=True)),
                ('slug', models.SlugField(blank=True, default=economia.models.get_RandomString, max_length=11, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Salario',
            fields=[
                ('id', models.CharField(default=economia.models.generate_uuid, editable=False, max_length=40, primary_key=True, serialize=False, unique=True)),
                ('amount', models.FloatField(max_length=10)),
                ('fecha_deposito', models.DateField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(blank=True, default=economia.models.get_RandomString, max_length=11, unique=True)),
                ('fk_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Operaciones',
            fields=[
                ('id', models.CharField(default=economia.models.generate_uuid, editable=False, max_length=40, primary_key=True, serialize=False, unique=True)),
                ('slug', models.SlugField(blank=True, default=economia.models.get_RandomString, max_length=11, unique=True)),
                ('fecha_operacion', models.DateField(default=django.utils.timezone.now)),
                ('des', models.CharField(max_length=100)),
                ('amount', models.FloatField(max_length=10)),
                ('fk_salario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='economia.salario')),
                ('fk_tipo_op', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='economia.tipo_op')),
                ('fk_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Deudas',
            fields=[
                ('id', models.CharField(default=economia.models.generate_uuid, editable=False, max_length=40, primary_key=True, serialize=False, unique=True)),
                ('slug', models.SlugField(blank=True, default=economia.models.get_RandomString, max_length=11, unique=True)),
                ('estado', models.CharField(blank=True, choices=[('Liquidada', 'Liquidada'), ('Pendiente', 'Pendiente')], max_length=20, null=True)),
                ('tipo', models.CharField(blank=True, choices=[('PRESTAMOS', 'Prestamo'), ('DEUDAS', 'Deudas')], max_length=20, null=True)),
                ('amount', models.FloatField(max_length=10)),
                ('fecha_operacion', models.DateField(default=django.utils.timezone.now)),
                ('des', models.CharField(max_length=100)),
                ('fk_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
