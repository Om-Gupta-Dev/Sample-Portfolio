# Generated by Django 3.0.8 on 2020-07-19 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortApp', '0002_auto_20200719_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Name',
            field=models.CharField(max_length=50),
        ),
    ]
