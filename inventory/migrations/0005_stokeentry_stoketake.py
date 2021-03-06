# Generated by Django 2.2 on 2020-07-22 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200722_0750'),
        ('location', '0003_auto_20200722_0804'),
        ('inventory', '0004_auto_20200722_0951'),
    ]

    operations = [
        migrations.CreateModel(
            name='StokeTake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('date', models.DateField(null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Company')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Location')),
            ],
        ),
        migrations.CreateModel(
            name='StokeEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(null=True)),
                ('approval', models.BooleanField(default=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Item')),
                ('stoke_take', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.StokeTake')),
            ],
        ),
    ]
