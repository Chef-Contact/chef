# Generated by Django 4.2.7 on 2024-03-08 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chef_pages', '0006_shop_tagline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='back_image',
            field=models.ImageField(blank=True, null=True, upload_to='back_image/', verbose_name='Фото заднего фона на сайте'),
        ),
    ]
