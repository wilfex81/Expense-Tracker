# Generated by Django 4.1.7 on 2023-04-06 19:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_transaction_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budgetcategorie',
            name='budget',
        ),
        migrations.RemoveField(
            model_name='budgetcategorie',
            name='date_budgeted',
        ),
        migrations.RemoveField(
            model_name='budgetcategorie',
            name='title',
        ),
        migrations.AddField(
            model_name='budgetcategorie',
            name='budget_amount',
            field=models.DecimalField(decimal_places=2, default=20.0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='budgetcategorie',
            name='budget_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 6, 19, 9, 45, 409296, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='budgetcategorie',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='budgetcategorie',
            name='name',
            field=models.CharField(default=datetime.datetime(2023, 4, 6, 19, 10, 11, 50169, tzinfo=datetime.timezone.utc), max_length=255),
            preserve_default=False,
        ),
    ]