# Generated by Django 4.1.7 on 2023-03-17 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gi_videogame_release',
            name='gameImage',
            field=models.ImageField(default=None, upload_to='gameImage/'),
        ),
    ]
