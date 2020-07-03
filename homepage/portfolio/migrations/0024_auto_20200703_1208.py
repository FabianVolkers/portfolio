# Generated by Django 3.0.7 on 2020-07-03 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0023_auto_20200703_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('url', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='section',
            name='nav_bar_link',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='FooterLink',
            fields=[
                ('link_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio.Link')),
                ('footer_section', models.CharField(max_length=64)),
            ],
            bases=('portfolio.link',),
        ),
        migrations.CreateModel(
            name='NavLink',
            fields=[
                ('link_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio.Link')),
                ('position', models.IntegerField()),
            ],
            bases=('portfolio.link',),
        ),
    ]
