# Generated by Django 2.1.2 on 2018-11-24 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='uer_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('user_pwd', models.CharField(max_length=40)),
                ('user_email', models.CharField(max_length=30)),
                ('accepter_name', models.CharField(max_length=10)),
                ('accepter_address', models.CharField(max_length=100)),
                ('accepter_postcode', models.CharField(max_length=6)),
                ('accepter_phone_number', models.CharField(max_length=11)),
            ],
        ),
    ]
