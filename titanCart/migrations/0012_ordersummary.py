# Generated by Django 3.0.4 on 2020-03-26 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('titanCart', '0011_featured_recomended'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Shipping_Name', models.CharField(blank=True, max_length=15, null=True)),
                ('Shipping_Country', models.CharField(blank=True, max_length=20, null=True)),
                ('Title', models.CharField(blank=True, max_length=10, null=True)),
                ('First_Name', models.CharField(max_length=10)),
                ('Last_Name', models.CharField(max_length=10)),
                ('Shipping_Address', models.CharField(max_length=40)),
                ('Shipping_Address_b', models.CharField(blank=True, max_length=40, null=True)),
                ('Zip', models.CharField(blank=True, max_length=10, null=True)),
                ('Phone', models.CharField(max_length=15)),
                ('Alt_Phone', models.CharField(blank=True, max_length=15, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]