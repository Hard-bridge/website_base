# Generated by Django 5.0.3 on 2024-04-13 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0003_new_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='count_like',
            field=models.IntegerField(default=0),
        ),
    ]
