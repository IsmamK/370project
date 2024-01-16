# Generated by Django 4.0.4 on 2023-12-07 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_order_payment_method'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('houseNo', models.CharField(max_length=10)),
                ('flatNo', models.CharField(max_length=10)),
                ('street', models.CharField(max_length=30)),
                ('additional', models.CharField(max_length=30)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipping_address', to='restaurant.order')),
            ],
        ),
    ]