# Generated by Django 3.1.5 on 2021-04-23 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='tags',
            field=models.ManyToManyField(to='tienda.Tags'),
        ),
    ]