# Generated by Django 2.2 on 2020-07-22 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200722_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseoder',
            name='status',
            field=models.CharField(choices=[('recieved', 'Received'), ('retuned', 'Returned'), ('shipping', 'Shipping')], max_length=2),
        ),
    ]
