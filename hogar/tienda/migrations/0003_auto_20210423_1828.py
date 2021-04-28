# Generated by Django 3.1.5 on 2021-04-23 18:28

from django.db import migrations, models
import tienda.model_ext.case
import tienda.model_ext.caseFan
import tienda.model_ext.cpu
import tienda.model_ext.generales
import tienda.model_ext.gpu
import tienda.model_ext.motherboard
import tienda.model_ext.ram
import tienda.models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_producto_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.CharField(default=tienda.models.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='chipset',
            name='id',
            field=models.CharField(default=tienda.model_ext.generales.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='id',
            field=models.CharField(default=tienda.model_ext.generales.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='connector',
            name='id',
            field=models.CharField(default=tienda.model_ext.caseFan.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='controller',
            name='id',
            field=models.CharField(default=tienda.model_ext.caseFan.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='cooling',
            name='id',
            field=models.CharField(default=tienda.model_ext.gpu.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='corefamily',
            name='id',
            field=models.CharField(default=tienda.model_ext.cpu.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='eccram',
            name='id',
            field=models.CharField(default=tienda.model_ext.ram.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='ethernet',
            name='id',
            field=models.CharField(default=tienda.model_ext.motherboard.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='externalpower',
            name='id',
            field=models.CharField(default=tienda.model_ext.gpu.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='formfactor',
            name='id',
            field=models.CharField(default=tienda.model_ext.generales.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='framesync',
            name='id',
            field=models.CharField(default=tienda.model_ext.gpu.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='frontpanelusb',
            name='id',
            field=models.CharField(default=tienda.model_ext.case.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='integrategraphic',
            name='id',
            field=models.CharField(default=tienda.model_ext.cpu.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='interface',
            name='id',
            field=models.CharField(default=tienda.model_ext.gpu.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='led',
            name='id',
            field=models.CharField(default=tienda.model_ext.caseFan.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='listacompra',
            name='id',
            field=models.CharField(default=tienda.models.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='listadeseos',
            name='id',
            field=models.CharField(default=tienda.models.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='id',
            field=models.CharField(default=tienda.model_ext.generales.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='memorytype',
            name='id',
            field=models.CharField(default=tienda.model_ext.motherboard.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='microarch',
            name='id',
            field=models.CharField(default=tienda.model_ext.cpu.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='powersupply',
            name='id',
            field=models.CharField(default=tienda.model_ext.case.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='id',
            field=models.CharField(default=tienda.models.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='serie',
            name='id',
            field=models.CharField(default=tienda.model_ext.cpu.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='id',
            field=models.CharField(default=tienda.models.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='sidepanelwindow',
            name='id',
            field=models.CharField(default=tienda.model_ext.case.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='size',
            name='id',
            field=models.CharField(default=tienda.model_ext.caseFan.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='sli',
            name='id',
            field=models.CharField(default=tienda.model_ext.generales.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='socket',
            name='id',
            field=models.CharField(default=tienda.model_ext.generales.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='tags',
            name='id',
            field=models.CharField(default=tienda.models.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='tiemposram',
            name='id',
            field=models.CharField(default=tienda.model_ext.ram.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='typecase',
            name='id',
            field=models.CharField(default=tienda.model_ext.case.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='typememory',
            name='id',
            field=models.CharField(default=tienda.model_ext.generales.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='typeproduct',
            name='id',
            field=models.CharField(default=tienda.model_ext.generales.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='wireless',
            name='id',
            field=models.CharField(default=tienda.model_ext.motherboard.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]