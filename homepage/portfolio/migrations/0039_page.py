# Generated by Django 3.0.7 on 2020-07-04 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0038_message_sent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('template_name', models.CharField(max_length=64)),
                ('nav_bar_link', models.BooleanField(default=True)),
                ('nav_link', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.NavLink')),
            ],
        ),
    ]
