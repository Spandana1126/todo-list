# Generated by Django 3.2.6 on 2021-08-04 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskingapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='status',
            field=models.CharField(default='incomplete', max_length=20),
        ),
    ]
