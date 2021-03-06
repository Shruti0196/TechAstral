# Generated by Django 3.2.9 on 2022-03-12 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20220312_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('amt', models.CharField(max_length=23)),
            ],
        ),
        migrations.AlterField(
            model_name='crowdfundingdetails',
            name='date',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='eventdetails',
            name='date',
            field=models.CharField(max_length=10),
        ),
    ]
