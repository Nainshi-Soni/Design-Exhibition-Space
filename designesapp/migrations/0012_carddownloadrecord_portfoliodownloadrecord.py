# Generated by Django 5.1 on 2025-06-01 19:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designesapp', '0011_downloadrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardDownloadRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
                ('download_count', models.IntegerField(default=0)),
                ('has_paid', models.BooleanField(default=False)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='designesapp.cards')),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioDownloadRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
                ('download_count', models.IntegerField(default=0)),
                ('has_paid', models.BooleanField(default=False)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='designesapp.portfolios')),
            ],
        ),
    ]
