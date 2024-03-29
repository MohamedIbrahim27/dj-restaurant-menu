# Generated by Django 4.2 on 2023-05-19 23:28

import creditcards.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodmenu', '0012_order_alter_bookatable_chooseaddresstable_and_more'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('adress', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20, verbose_name='phone')),
                ('cardholder', models.CharField(max_length=20, verbose_name='Card Holder')),
                ('cardnumber', creditcards.models.CardNumberField(max_length=16, verbose_name='Card Number')),
                ('expire', creditcards.models.CardExpiryField(verbose_name='Exepire Date')),
                ('security', creditcards.models.SecurityCodeField(max_length=4, verbose_name='CCV')),
                ('order_delivery_date', models.DateTimeField(blank=True, null=True, verbose_name='Delivery Date')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodmenu.order')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
    ]
