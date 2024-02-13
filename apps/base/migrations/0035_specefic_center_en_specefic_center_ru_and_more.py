# Generated by Django 4.2.7 on 2024-02-13 04:37

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0034_alter_perfect_options_hospitaly_descriptions_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='specefic',
            name='center_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Центр'),
        ),
        migrations.AddField(
            model_name='specefic',
            name='center_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Центр'),
        ),
        migrations.AddField(
            model_name='specefic',
            name='descriptions_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='specefic',
            name='descriptions_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='specefic',
            name='image_en',
            field=models.ImageField(null=True, upload_to='specefic', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='specefic',
            name='image_ru',
            field=models.ImageField(null=True, upload_to='specefic', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='specefic',
            name='title_about_diets_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовка О ДИЕТАХ'),
        ),
        migrations.AddField(
            model_name='specefic',
            name='title_about_diets_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовка О ДИЕТАХ'),
        ),
        migrations.AddField(
            model_name='specefic',
            name='title_allergens_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовка allergens '),
        ),
        migrations.AddField(
            model_name='specefic',
            name='title_allergens_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовка allergens '),
        ),
        migrations.AddField(
            model_name='specefic',
            name='title_diets_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовка diets '),
        ),
        migrations.AddField(
            model_name='specefic',
            name='title_diets_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовка diets '),
        ),
        migrations.AddField(
            model_name='specefic',
            name='title_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка'),
        ),
        migrations.AddField(
            model_name='specefic',
            name='title_filters_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовка filters '),
        ),
        migrations.AddField(
            model_name='specefic',
            name='title_filters_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовка filters '),
        ),
        migrations.AddField(
            model_name='specefic',
            name='title_list_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовка list '),
        ),
        migrations.AddField(
            model_name='specefic',
            name='title_list_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовка list '),
        ),
        migrations.AddField(
            model_name='specefic',
            name='title_offered_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовка offered '),
        ),
        migrations.AddField(
            model_name='specefic',
            name='title_offered_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовка offered '),
        ),
        migrations.AddField(
            model_name='specefic',
            name='title_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка'),
        ),
    ]
