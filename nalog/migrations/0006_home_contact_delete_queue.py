# Generated by Django 4.2.11 on 2024-05-05 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nalog', '0005_alter_queue_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='home_contact',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='nalog.basemodel')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
            bases=('nalog.basemodel',),
        ),
        migrations.DeleteModel(
            name='Queue',
        ),
    ]
