# Generated by Django 3.0.7 on 2020-07-06 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0073_auto_20200706_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectionitem',
            name='image_alttext',
            field=models.TextField(default='Image of <django.db.models.fields.CharField>'),
        ),
    ]
