# Generated by Django 4.2.11 on 2024-05-05 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nalog', '0004_alter_queue_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='date',
            field=models.DateField(),
        ),
    ]
