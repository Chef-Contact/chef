# Generated by Django 4.2.7 on 2024-02-12 19:12

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0033_become_descriptions_en_become_descriptions_ru_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='perfect',
            options={'verbose_name': 'Найдите идеальную еду', 'verbose_name_plural': 'Найдите идеальную еду '},
        ),
        migrations.AddField(
            model_name='hospitaly',
            name='descriptions_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='hospitaly',
            name='descriptions_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='hospitaly',
            name='image_en',
            field=models.ImageField(null=True, upload_to='hospitaly', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='hospitaly',
            name='image_ru',
            field=models.ImageField(null=True, upload_to='hospitaly', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='hospitaly',
            name='quests_all2_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание 3'),
        ),
        migrations.AddField(
            model_name='hospitaly',
            name='quests_all2_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание 3'),
        ),
        migrations.AddField(
            model_name='hospitaly',
            name='quests_all3_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание 4'),
        ),
        migrations.AddField(
            model_name='hospitaly',
            name='quests_all3_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание 4'),
        ),
        migrations.AddField(
            model_name='hospitaly',
            name='quests_all_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание 2'),
        ),
        migrations.AddField(
            model_name='hospitaly',
            name='quests_all_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание 2'),
        ),
        migrations.AddField(
            model_name='hospitaly',
            name='quests_title_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка GUESTS '),
        ),
        migrations.AddField(
            model_name='hospitaly',
            name='quests_title_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка GUESTS '),
        ),
        migrations.AddField(
            model_name='hospitaly',
            name='title_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка'),
        ),
        migrations.AddField(
            model_name='hospitaly',
            name='title_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка'),
        ),
        migrations.AddField(
            model_name='howitworks',
            name='descriptions_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='howitworks',
            name='descriptions_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='howitworks',
            name='image_en',
            field=models.ImageField(null=True, upload_to='howitworks/'),
        ),
        migrations.AddField(
            model_name='howitworks',
            name='image_ru',
            field=models.ImageField(null=True, upload_to='howitworks/'),
        ),
        migrations.AddField(
            model_name='howitworks',
            name='title2_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка WORK'),
        ),
        migrations.AddField(
            model_name='howitworks',
            name='title2_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка WORK'),
        ),
        migrations.AddField(
            model_name='howitworks',
            name='title3_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка 3'),
        ),
        migrations.AddField(
            model_name='howitworks',
            name='title3_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка 3'),
        ),
        migrations.AddField(
            model_name='howitworks',
            name='title4_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка 4'),
        ),
        migrations.AddField(
            model_name='howitworks',
            name='title4_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка 4'),
        ),
        migrations.AddField(
            model_name='howitworks',
            name='title_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка'),
        ),
        migrations.AddField(
            model_name='howitworks',
            name='title_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка'),
        ),
    ]
