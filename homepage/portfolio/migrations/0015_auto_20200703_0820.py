# Generated by Django 3.0.7 on 2020-07-03 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_baseentry_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('slug', models.SlugField(editable=False)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SectionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('template_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.RemoveField(
            model_name='baseentry',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='section',
            name='section_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.SectionType'),
        ),
        migrations.AddField(
            model_name='baseentry',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.Section'),
        ),
    ]
