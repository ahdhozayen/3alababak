# Generated by Django 2.2 on 2020-07-21 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0003_auto_20200721_0942'),
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('zip_code', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=30)),
                ('landline', models.CharField(max_length=30)),
                ('number_of_products', models.IntegerField()),
                ('manager_name', models.CharField(max_length=30)),
                ('manager_mail', models.EmailField(max_length=254)),
                ('manager_phone_number', models.CharField(max_length=30)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.company')),
            ],
        ),
    ]
