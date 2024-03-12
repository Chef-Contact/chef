# Generated by Django 4.2.7 on 2024-02-28 18:03

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0002_delete_chefregister'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='question_10',
        ),
        migrations.RemoveField(
            model_name='host',
            name='question_10_en',
        ),
        migrations.RemoveField(
            model_name='host',
            name='question_10_ru',
        ),
        migrations.RemoveField(
            model_name='host',
            name='question_11',
        ),
        migrations.RemoveField(
            model_name='host',
            name='question_11_en',
        ),
        migrations.RemoveField(
            model_name='host',
            name='question_11_ru',
        ),
        migrations.RemoveField(
            model_name='host',
            name='question_12',
        ),
        migrations.RemoveField(
            model_name='host',
            name='question_12_en',
        ),
        migrations.RemoveField(
            model_name='host',
            name='question_12_ru',
        ),
        migrations.RemoveField(
            model_name='host',
            name='question_13',
        ),
        migrations.RemoveField(
            model_name='host',
            name='question_13_en',
        ),
        migrations.RemoveField(
            model_name='host',
            name='question_13_ru',
        ),
        migrations.RemoveField(
            model_name='host',
            name='question_14',
        ),
        migrations.RemoveField(
            model_name='host',
            name='question_14_en',
        ),
        migrations.RemoveField(
            model_name='host',
            name='question_14_ru',
        ),
        migrations.RemoveField(
            model_name='host',
            name='question_15',
        ),
        migrations.RemoveField(
            model_name='host',
            name='question_15_en',
        ),
        migrations.RemoveField(
            model_name='host',
            name='question_15_ru',
        ),
        migrations.RemoveField(
            model_name='host',
            name='question_16',
        ),
        migrations.RemoveField(
            model_name='host',
            name='question_16_en',
        ),
        migrations.RemoveField(
            model_name='host',
            name='question_16_ru',
        ),
        migrations.RemoveField(
            model_name='host',
            name='question_17',
        ),
        migrations.RemoveField(
            model_name='host',
            name='question_17_en',
        ),
        migrations.RemoveField(
            model_name='host',
            name='question_17_ru',
        ),
        migrations.RemoveField(
            model_name='host',
            name='question_18',
        ),
        migrations.RemoveField(
            model_name='host',
            name='question_18_en',
        ),
        migrations.RemoveField(
            model_name='host',
            name='question_18_ru',
        ),
        migrations.RemoveField(
            model_name='host',
            name='question_9',
        ),
        migrations.RemoveField(
            model_name='host',
            name='question_9_en',
        ),
        migrations.RemoveField(
            model_name='host',
            name='question_9_ru',
        ),
        migrations.AlterField(
            model_name='host',
            name='question_3',
            field=models.CharField(max_length=155, verbose_name='Цена продукта'),
        ),
        migrations.AlterField(
            model_name='host',
            name='question_3_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Цена продукта'),
        ),
        migrations.AlterField(
            model_name='host',
            name='question_3_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Цена продукта'),
        ),
        migrations.AlterField(
            model_name='host',
            name='question_4',
            field=models.CharField(max_length=155, verbose_name='Цена доставки'),
        ),
        migrations.AlterField(
            model_name='host',
            name='question_4_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Цена доставки'),
        ),
        migrations.AlterField(
            model_name='host',
            name='question_4_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Цена доставки'),
        ),
        migrations.AlterField(
            model_name='host',
            name='question_5',
            field=models.CharField(max_length=155, verbose_name='Дайте название вашему продукту'),
        ),
        migrations.AlterField(
            model_name='host',
            name='question_5_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Дайте название вашему продукту'),
        ),
        migrations.AlterField(
            model_name='host',
            name='question_5_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Дайте название вашему продукту'),
        ),
        migrations.AlterField(
            model_name='host',
            name='question_6',
            field=models.CharField(max_length=155, verbose_name='Напишите подробное описание продукта'),
        ),
        migrations.AlterField(
            model_name='host',
            name='question_6_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Напишите подробное описание продукта'),
        ),
        migrations.AlterField(
            model_name='host',
            name='question_6_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Напишите подробное описание продукта'),
        ),
        migrations.AlterField(
            model_name='host',
            name='question_7',
            field=models.CharField(max_length=155, verbose_name='Добавьте фотографии продукта'),
        ),
        migrations.AlterField(
            model_name='host',
            name='question_7_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Добавьте фотографии продукта'),
        ),
        migrations.AlterField(
            model_name='host',
            name='question_7_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Добавьте фотографии продукта'),
        ),
        migrations.AlterField(
            model_name='host',
            name='question_8',
            field=ckeditor.fields.RichTextField(verbose_name='Дополнительные фотографии продукта'),
        ),
        migrations.AlterField(
            model_name='host',
            name='question_8_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Дополнительные фотографии продукта'),
        ),
        migrations.AlterField(
            model_name='host',
            name='question_8_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Дополнительные фотографии продукта'),
        ),
    ]
