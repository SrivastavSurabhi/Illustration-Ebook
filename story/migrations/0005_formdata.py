# Generated by Django 3.2.19 on 2023-09-08 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0004_alter_response_unique_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(max_length=1000)),
                ('response_id', models.CharField(blank=True, max_length=1000, null=True)),
                ('readers_name', models.CharField(max_length=1000)),
                ('story_format', models.CharField(max_length=1000)),
                ('genre', models.CharField(max_length=1000)),
                ('writing_style', models.CharField(max_length=1000)),
                ('charcter_type', models.CharField(max_length=1000)),
                ('charachter_name', models.CharField(max_length=1000)),
                ('charachter_age', models.CharField(blank=True, max_length=1000, null=True)),
                ('charachter_ethinicity', models.CharField(blank=True, max_length=1000, null=True)),
                ('animal_type', models.CharField(blank=True, max_length=1000, null=True)),
                ('readers_age_group', models.CharField(choices=[('Little Sprouts (Age 3 - 5) 🌱', '3-5 years'), ('Young Adventurers (Age 6 - 8) 🌟', '6-8 years'), ('Valiant Explorers (Age 9 - 12) 🗺️', '9-12 years'), ('Teenage Trailblazers (Age 13 - 15) 🚀', '13-15 years'), ('Timeless Tales for All (Age 16+) 🌍', '16+ years')], max_length=1000)),
                ('location', models.CharField(max_length=1000)),
                ('moral', models.CharField(max_length=1000)),
                ('audio_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]