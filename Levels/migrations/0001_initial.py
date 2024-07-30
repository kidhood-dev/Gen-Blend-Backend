# Generated by Django 5.0.7 on 2024-07-30 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('level_name', models.CharField(max_length=50)),
                ('max_score', models.IntegerField(blank=True, null=True)),
                ('min_score', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('max_score', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LevelAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('total_attempt_count', models.IntegerField(blank=True, null=True)),
                ('attempts_to_unlock_next_level', models.IntegerField(blank=True, null=True)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='level_attempts', to='Levels.level')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
