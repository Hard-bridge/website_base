# Generated by Django 5.0.3 on 2024-04-06 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='image',
            field=models.ImageField(default='news/defailt.png', upload_to='news/'),
        ),
    ]