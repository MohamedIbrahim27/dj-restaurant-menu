# Generated by Django 4.2 on 2023-07-06 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_paypalpayment_address_paypalpayment_not_if_any_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paypalpayment',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
