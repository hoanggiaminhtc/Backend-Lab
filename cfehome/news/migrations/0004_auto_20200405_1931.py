# Generated by Django 3.0.4 on 2020-04-05 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_date_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='date_time',
            new_name='date',
        ),
    ]