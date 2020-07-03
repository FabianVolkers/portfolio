# Generated by Django 3.0.7 on 2020-07-03 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0020_auto_20200703_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseentry',
            name='detail_view',
            field=models.CharField(choices=[('portfolio.views.ProjectView', 'Project View'), ('portfolio.views.PhotoView', 'Photo View'), ('portfolio.views.BaseEntry', 'Base View')], default='portfolio.views.BaseEntryView', max_length=64),
        ),
    ]
