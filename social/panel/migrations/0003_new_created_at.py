# Generated by Django 5.0.3 on 2024-04-13 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0002_new_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
