# Generated by Django 4.1.7 on 2023-04-22 10:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='date_recorded',
            field=models.DateField(default=datetime.datetime(2023, 4, 22, 10, 11, 37, 901509, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]