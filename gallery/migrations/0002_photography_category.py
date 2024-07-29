# Generated by Django 5.0.7 on 2024-07-29 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photography',
            name='category',
            field=models.CharField(choices=[('NEBULOSA', 'Nebulosa'), ('ESTRELA', 'Estrela'), ('GALÁXIA', 'Gálaxia'), ('PLANETA', 'Planeta')], default='', max_length=100),
        ),
    ]
