# Generated by Django 5.1.1 on 2024-10-16 10:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('takoyaki', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='takoyakimenu',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(1.0)]),
        ),
    ]
