# Generated by Django 3.0.7 on 2020-07-03 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0026_link_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='view',
            field=models.CharField(choices=[('portfolio:project-detail', 'Project View'), ('portfolio:photo-detail', 'Photo View'), ('portfolio:entry-detail', 'Base View')], default='portfolio:entry-detail', max_length=64),
        ),
    ]
