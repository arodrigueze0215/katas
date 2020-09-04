# Generated by Django 3.1 on 2020-09-04 03:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0007_remove_customer_customer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='account_id',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='credit',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='debit',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
