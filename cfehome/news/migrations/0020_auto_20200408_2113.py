# Generated by Django 3.0.4 on 2020-04-08 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0019_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image_2',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='news',
            name='image_3',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='news',
            name='image_4',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
