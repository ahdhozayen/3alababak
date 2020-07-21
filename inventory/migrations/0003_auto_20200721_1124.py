# Generated by Django 2.2 on 2020-07-21 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
        ('account', '0003_auto_20200721_0942'),
        ('inventory', '0002_auto_20200721_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('display_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UOM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.company')),
            ],
        ),
        migrations.AlterField(
            model_name='brand',
            name='description',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='UOM',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.UOM'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.CreateModel(
            name='product_attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.attribute')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
            ],
        ),
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.FileField(upload_to='uploads/')),
                ('description', models.CharField(blank=True, max_length=30, null=True)),
                ('quantity', models.IntegerField()),
                ('avg_cost', models.DecimalField(decimal_places=3, max_digits=10000)),
                ('selling_price', models.DecimalField(decimal_places=3, max_digits=10000)),
                ('SKU', models.CharField(max_length=30)),
                ('barcode', models.CharField(max_length=30)),
                ('tax', models.BooleanField(max_length=30)),
                ('UOM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.UOM')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.location')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
            ],
        ),
    ]
