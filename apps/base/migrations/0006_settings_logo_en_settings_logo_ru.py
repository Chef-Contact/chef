# Generated by Django 4.2.7 on 2024-03-17 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_settings_logo_alter_settings_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='logo_en',
            field=models.ImageField(null=True, upload_to='logo/', verbose_name='Логотип сайта'),
        ),
        migrations.AddField(
            model_name='settings',
            name='logo_ru',
            field=models.ImageField(null=True, upload_to='logo/', verbose_name='Логотип сайта'),
        ),
    ]