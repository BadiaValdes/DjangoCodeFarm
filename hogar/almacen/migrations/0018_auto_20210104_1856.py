# Generated by Django 3.1.4 on 2021-01-04 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0017_auto_20210104_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marca',
            name='user',
        ),
        migrations.RemoveField(
            model_name='posicion',
            name='user',
        ),
        migrations.RemoveField(
            model_name='productotipo',
            name='user',
        ),
        migrations.AlterField(
            model_name='reportes',
            name='slug_url',
            field=models.SlugField(blank=True, default='R7jbVYQrb7h6mxHS851q8yFw007dkXcngpLnfz19', max_length=40, unique=True),
        ),
    ]