# Generated by Django 3.0.7 on 2020-07-05 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0040_auto_20200705_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseentry',
            name='translantions_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.TranslationsGroup'),
        ),
        migrations.AddField(
            model_name='section',
            name='translantions_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.TranslationsGroup'),
        ),
        migrations.DeleteModel(
            name='Translatable',
        ),
    ]
