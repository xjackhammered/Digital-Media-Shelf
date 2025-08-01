# Generated by Django 5.2.4 on 2025-07-30 07:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MediaItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('movie', 'Movie'), ('game', 'Game'), ('series', 'Series'), ('book', 'Book')], max_length=10)),
                ('status', models.CharField(choices=[('completed', 'Completed'), ('watching', 'Watching'), ('wishlisted', 'Wishlisted'), ('dropped', 'Dropped')], max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('genres', models.ManyToManyField(to='api.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=100)),
                ('rating', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='api.mediaitem')),
            ],
        ),
    ]
