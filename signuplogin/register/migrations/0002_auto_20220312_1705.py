# Generated by Django 3.2.9 on 2022-03-12 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('date', models.DateField(max_length=1000)),
                ('time', models.TimeField(max_length=1000)),
                ('location', models.TextField(max_length=1000)),
                ('type1', models.TextField(max_length=1000)),
                ('desc', models.TextField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='admin_reg',
            name='area',
            field=models.CharField(default='', max_length=1255),
        ),
        migrations.AddField(
            model_name='admin_reg',
            name='phone',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='admin_reg',
            name='pincode',
            field=models.CharField(default='', max_length=255),
        ),
    ]