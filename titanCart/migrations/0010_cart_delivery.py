# Generated by Django 3.0.4 on 2020-03-26 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titanCart', '0009_auto_20200326_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='delivery',
            field=models.FloatField(default=10, null=True),
        ),
    ]
