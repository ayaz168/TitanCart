# Generated by Django 3.0.4 on 2020-04-09 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titanCart', '0014_ordersummary_shippingnote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('D', 'Default'), ('EL', 'Electronics'), ('En', 'Entairtnment'), ('H&F', 'Health and Fitness'), ('M', 'Mens Clothes'), ('W', 'Womens Clothes'), ('KC', 'Kids Clothes'), ('SE', 'Security'), ('WA', 'Watches'), ('SH', 'Shoes')], max_length=4),
        ),
    ]