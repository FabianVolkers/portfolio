# Generated by Django 3.0.7 on 2020-07-12 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0102_remove_sectiontype_template_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectiontype',
            name='template_name',
            field=models.CharField(default='portfolio/section.html', max_length=64),
            preserve_default=False,
        ),
    ]
