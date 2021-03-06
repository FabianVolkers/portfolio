# Generated by Django 3.0.7 on 2020-06-30 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('cover_photo', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='collection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.Collection'),
        ),
    ]
