# Generated by Django 4.2 on 2023-05-02 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_food', models.CharField(max_length=35)),
                ('contant_food', models.TextField()),
                ('Prise_food', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image_food', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('active_food', models.BooleanField(default=True)),
            ],
        ),
    ]
