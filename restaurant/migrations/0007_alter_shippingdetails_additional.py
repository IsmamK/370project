# Generated by Django 4.0.4 on 2023-12-07 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_shippingdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingdetails',
            name='additional',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
