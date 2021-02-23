# Generated by Django 3.1.4 on 2021-01-04 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('almacen', '0016_auto_20210104_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='posicion',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productotipo',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reportes',
            name='slug_url',
            field=models.SlugField(blank=True, default='ZChjkRBpcSkCghJjvx5rdRd6vxHlYypQfN8pNZSb', max_length=40, unique=True),
        ),
    ]
