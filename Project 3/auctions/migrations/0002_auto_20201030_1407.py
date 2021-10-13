# Generated by Django 3.0.8 on 2020-10-30 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=5, max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='listings',
            name='url',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='listings',
            name='category',
            field=models.ForeignKey(blank=True, default=5, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='Item_category', to='auctions.Category'),
        ),
    ]