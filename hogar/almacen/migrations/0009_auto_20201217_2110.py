# Generated by Django 3.1.4 on 2020-12-17 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0008_remove_reportes_file_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportes',
            name='nombre',
            field=models.CharField(default='hola', max_length=50),
        ),
    ]
