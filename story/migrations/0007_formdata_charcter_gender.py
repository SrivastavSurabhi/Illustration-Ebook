# Generated by Django 3.2.19 on 2023-09-08 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0006_formdata_ebook_format'),
    ]

    operations = [
        migrations.AddField(
            model_name='formdata',
            name='charcter_gender',
            field=models.CharField(blank=True, choices=[('Boy 🚶\u200d♂️', 'Boy'), ('Girl 🚶\u200d♀️', 'Girl'), ('Prefer not to specify 🌟', 'Prefer not to specify')], max_length=1000, null=True),
        ),
    ]