# Generated by Django 3.0 on 2019-12-15 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=10)),
                ('make', models.CharField(max_length=10)),
                ('model', models.CharField(max_length=20)),
                ('typev', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
                ('dementions', models.TextField()),
                ('weight', models.CharField(max_length=40)),
            ],
        ),
    ]
