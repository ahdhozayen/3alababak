# Generated by Django 2.2 on 2020-08-06 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20200722_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseoder',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='purchaseoder',
            name='last_updated_at',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseoder',
            name='last_updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]