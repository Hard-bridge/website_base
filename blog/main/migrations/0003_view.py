# Generated by Django 5.0.2 on 2024-08-02 08:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('new', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.news')),
            ],
        ),
    ]