# Generated by Django 5.0.6 on 2024-12-05 05:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_list', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppinglist',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]