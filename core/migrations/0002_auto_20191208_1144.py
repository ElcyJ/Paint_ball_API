# Generated by Django 2.2.7 on 2019-12-08 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gun',
            name='number',
            field=models.CharField(max_length=4),
        ),
    ]
