# Generated by Django 3.0.4 on 2020-04-09 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titanCart', '0013_auto_20200326_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordersummary',
            name='ShippingNote',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
