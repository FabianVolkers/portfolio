# Generated by Django 3.0.7 on 2020-07-03 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0019_auto_20200703_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sectiontype',
            name='detail_view',
        ),
        migrations.AddField(
            model_name='baseentry',
            name='detail_view',
            field=models.CharField(default='portfolio:entry-detail', max_length=64),
        ),
    ]
