# Generated by Django 4.2.7 on 2024-02-19 19:18

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chef_pages', '0003_alter_shop_back_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Подробное описание о вас'),
        ),
    ]
