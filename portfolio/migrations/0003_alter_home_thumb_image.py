# Generated by Django 4.0.6 on 2022-08-02 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_remove_about_content_remove_about_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='thumb_image',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]