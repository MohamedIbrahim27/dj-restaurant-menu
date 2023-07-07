# Generated by Django 4.2 on 2023-07-06 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_mastercartpayment_paypalpayment_pttbankpayment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paypalpayment',
            name='address',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paypalpayment',
            name='not_if_any',
            field=models.CharField(default='exit', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paypalpayment',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
