# Generated by Django 5.0.6 on 2024-08-29 15:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_alter_comment_options_comment_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlist',
            name='category',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='auctions.category'),
        ),
    ]
