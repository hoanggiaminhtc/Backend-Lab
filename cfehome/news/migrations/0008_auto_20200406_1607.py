# Generated by Django 3.0.4 on 2020-04-06 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20200406_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
