# Generated by Django 4.2 on 2023-05-05 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodmenu', '0007_restaurantmenu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurantmenu',
            name='Assess',
        ),
    ]
