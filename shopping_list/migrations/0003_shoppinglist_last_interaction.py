# Generated by Django 5.0.6 on 2024-12-10 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_list', '0002_shoppinglist_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppinglist',
            name='last_interaction',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
