# Generated by Django 3.1.5 on 2021-04-26 20:43

from django.db import migrations, models
import tienda.model_ext.generales


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0004_auto_20210426_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='slug',
            field=models.SlugField(blank=True, default=tienda.model_ext.generales.get_RandomString, max_length=25, unique=True),
        ),
    ]
