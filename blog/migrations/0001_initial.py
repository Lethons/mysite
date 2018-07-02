# Generated by Django 2.0.6 on 2018-07-02 07:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('publish_time', models.DateField(default=datetime.datetime)),
                ('update_time', models.DateField(auto_now=True)),
                ('is_commend', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Tag'),
        ),
    ]