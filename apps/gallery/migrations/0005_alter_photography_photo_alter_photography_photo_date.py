# Generated by Django 5.0.7 on 2024-07-30 22:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_photography_photo_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photography',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='photography',
            name='photo_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 30, 19, 17, 46, 707709)),
        ),
    ]