# Generated by Django 4.0.2 on 2022-02-08 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=None),
        ),
    ]
