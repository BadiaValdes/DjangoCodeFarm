# Generated by Django 3.1.4 on 2021-01-07 19:36

import almacen.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0019_auto_20210107_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportes',
            name='slug_url',
            field=models.SlugField(blank=True, default=almacen.models.get_RandomString, max_length=40, unique=True),
        ),
    ]