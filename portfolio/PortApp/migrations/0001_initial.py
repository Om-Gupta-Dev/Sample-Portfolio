# Generated by Django 3.0.8 on 2020-07-11 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=15)),
                ('Last_name', models.CharField(max_length=15)),
                ('Username', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('Message', models.TextField()),
            ],
        ),
    ]
