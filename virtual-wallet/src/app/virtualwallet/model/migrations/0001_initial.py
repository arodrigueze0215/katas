# Generated by Django 3.1 on 2020-08-30 19:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('opening_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('firs_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('person_number', models.CharField(max_length=500)),
                ('phone_number', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Debit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ammount', models.PositiveIntegerField()),
                ('transaction_date', models.DateField()),
                ('description', models.CharField(max_length=1500)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.account')),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ammount', models.PositiveIntegerField()),
                ('transaction_date', models.DateField()),
                ('description', models.CharField(max_length=1500)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.account')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.customer'),
        ),
    ]
