# Generated by Django 3.1 on 2020-09-04 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0003_customer_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]