# Generated by Django 3.0.7 on 2020-07-06 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0058_auto_20200706_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
