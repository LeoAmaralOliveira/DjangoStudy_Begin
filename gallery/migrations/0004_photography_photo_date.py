# Generated by Django 5.0.7 on 2024-07-29 23:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_photography_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='photography',
            name='photo_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 29, 20, 35, 54, 963416)),
        ),
    ]
