# Generated by Django 4.2.7 on 2024-02-14 08:17

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0002_host_question_15_host_question_16_host_question_17_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='question_18',
            field=ckeditor.fields.RichTextField(verbose_name='Страница подтверждения данных'),
        ),
    ]