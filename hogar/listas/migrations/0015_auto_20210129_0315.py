# Generated by Django 3.1.5 on 2021-01-29 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listas', '0014_auto_20210129_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lista',
            name='nb',
            field=models.CharField(default='Lista 9QdS8', max_length=30),
        ),
        migrations.AlterField(
            model_name='lista',
            name='slugUrl',
            field=models.SlugField(default='KgC6wPBpWPC', editable=False, max_length=20, unique=True),
        ),
    ]