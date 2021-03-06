# Generated by Django 3.2.9 on 2021-11-18 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoId', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('publishedAt', models.DateTimeField(auto_now_add=True)),
                ('thumbnail_url', models.URLField()),
            ],
        ),
    ]
