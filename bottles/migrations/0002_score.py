# Generated by Django 5.0.2 on 2024-08-16 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bottles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('email', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
    ]
