# Generated by Django 4.2.7 on 2024-02-13 00:52

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_alter_perfectactive_options_perfectactive_foreign'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospitaly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовка')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='hospitaly', verbose_name='Фото')),
                ('quests_title', models.CharField(max_length=155, verbose_name='Заголовка GUESTS ')),
                ('quests_all', ckeditor.fields.RichTextField(verbose_name='Описание 2')),
            ],
            options={
                'verbose_name_plural': 'ГОСТЕПРИИМСТВО',
            },
        ),
    ]
