# Generated by Django 3.0.8 on 2020-11-24 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20201124_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='category',
            field=models.ForeignKey(blank=True, default=5, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='Item_category', to='auctions.Category'),
        ),
    ]
