# Generated by Django 3.0.7 on 2020-07-06 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0064_auto_20200706_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectioncommon',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sections', to='portfolio.Page'),
        ),
    ]
