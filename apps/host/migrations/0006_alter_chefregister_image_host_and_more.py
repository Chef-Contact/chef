# Generated by Django 4.2.7 on 2024-02-14 09:31

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0005_alter_chefregister_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chefregister',
            name='image_host',
            field=models.ImageField(blank=True, null=True, upload_to='image_host/', verbose_name='фотография в объявлении'),
        ),
        migrations.AlterField(
            model_name='chefregister',
            name='question_1',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Тип услуги'),
        ),
        migrations.AlterField(
            model_name='chefregister',
            name='question_10',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Сумма с гостей'),
        ),
        migrations.AlterField(
            model_name='chefregister',
            name='question_11',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Дайте название вашему объявлению'),
        ),
        migrations.AlterField(
            model_name='chefregister',
            name='question_12',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Напишите подробное описание объявления'),
        ),
        migrations.AlterField(
            model_name='chefregister',
            name='question_2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип кухни'),
        ),
        migrations.AlterField(
            model_name='chefregister',
            name='question_3',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Местоположение'),
        ),
        migrations.AlterField(
            model_name='chefregister',
            name='question_4',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Дополнительные услуги'),
        ),
        migrations.AlterField(
            model_name='chefregister',
            name='question_5',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Доставка заказа'),
        ),
        migrations.AlterField(
            model_name='chefregister',
            name='question_6',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Соблюдение диеты'),
        ),
        migrations.AlterField(
            model_name='chefregister',
            name='question_7',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Аллергены'),
        ),
        migrations.AlterField(
            model_name='chefregister',
            name='question_8',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Гостей максимум'),
        ),
        migrations.AlterField(
            model_name='chefregister',
            name='question_9',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Гостей минимум'),
        ),
    ]
