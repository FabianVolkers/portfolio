# Generated by Django 3.0.7 on 2020-07-11 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0088_contactresponse_contactresponsecommon'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactresponse',
            name='common',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.ContactResponseCommon'),
        ),
    ]
