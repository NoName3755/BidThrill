# Generated by Django 5.0.6 on 2024-10-08 14:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_alter_auctionlist_image_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auctionlist',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='auctionlist',
            name='category',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='auctions.category'),
        ),
    ]
