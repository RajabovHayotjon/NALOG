# Generated by Django 4.2.11 on 2024-05-19 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_loginus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginus',
            name='user',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='registerus',
            name='user',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
