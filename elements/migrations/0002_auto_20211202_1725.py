# Generated by Django 3.2.9 on 2021-12-02 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='element',
            name='horizontal_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='element',
            name='vertical_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='element',
            name='why',
            field=models.TextField(null=True),
        ),
    ]
