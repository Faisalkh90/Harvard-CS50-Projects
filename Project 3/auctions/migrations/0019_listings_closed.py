# Generated by Django 3.0.8 on 2020-12-08 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_auto_20201201_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]
