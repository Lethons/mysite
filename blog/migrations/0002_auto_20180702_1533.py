# Generated by Django 2.0.6 on 2018-07-02 07:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish_time',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]