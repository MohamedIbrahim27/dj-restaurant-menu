# Generated by Django 4.2 on 2023-07-05 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_productfavorites'),
    ]

    operations = [
        migrations.CreateModel(
            name='Static_Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_address', models.CharField(max_length=150)),
                ('cost', models.CharField(max_length=50)),
                ('distance', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='adress',
        ),
        migrations.AddField(
            model_name='profile',
            name='NotesIf_any',
            field=models.CharField(default='', max_length=500, verbose_name='Notes'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150, verbose_name='detail for Static Address')),
                ('sta_address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.static_address', verbose_name='Static Address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile', verbose_name='user')),
            ],
        ),
    ]
