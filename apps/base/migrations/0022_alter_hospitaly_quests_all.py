# Generated by Django 4.2.7 on 2024-02-13 00:54

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_hospitaly'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitaly',
            name='quests_all',
            field=ckeditor.fields.RichTextField(verbose_name='Описание 4'),
        ),
    ]
