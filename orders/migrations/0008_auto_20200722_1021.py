# Generated by Django 2.2 on 2020-07-22 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20200722_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseoder',
            name='status',
            field=models.CharField(choices=[('recieved', 'Received'), ('retuned', 'Returned'), ('shipping', 'Shipping')], max_length=8),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='status',
            field=models.CharField(choices=[('recieved', 'Received'), ('retuned', 'Returned'), ('shipping', 'Shipping')], max_length=8),
        ),
    ]
