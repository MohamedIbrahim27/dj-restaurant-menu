# Generated by Django 4.2 on 2023-07-06 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_alter_paypalpayment_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mastercartpayment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='paypalpayment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='pttbankpayment',
            name='user',
        ),
        migrations.AlterField(
            model_name='paypalpayment',
            name='address',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AlterField(
            model_name='paypalpayment',
            name='not_if_any',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AlterField(
            model_name='paypalpayment',
            name='phone',
            field=models.CharField(default='None', max_length=50),
        ),
    ]
