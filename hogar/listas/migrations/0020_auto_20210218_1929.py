# Generated by Django 3.1.5 on 2021-02-18 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listas', '0019_auto_20210218_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lista',
            name='nb',
            field=models.CharField(default='Lista LkxZ9', max_length=30),
        ),
        migrations.AlterField(
            model_name='lista',
            name='slugUrl',
            field=models.SlugField(default='DLDtgjg-9kx', editable=False, max_length=20, unique=True),
        ),
    ]
