# Generated by Django 3.0.8 on 2020-07-18 14:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hireDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
