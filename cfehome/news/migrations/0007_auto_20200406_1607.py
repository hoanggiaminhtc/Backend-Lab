# Generated by Django 3.0.4 on 2020-04-06 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20200406_1607'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='image_title',
            new_name='image',
        ),
    ]
