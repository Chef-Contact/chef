# Generated by Django 4.2.7 on 2024-02-10 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_become_descriptions_alter_become_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_banner', models.CharField(max_length=155, verbose_name='Заголовка баннера')),
                ('title_banner_en', models.CharField(max_length=155, null=True, verbose_name='Заголовка баннера')),
                ('title_banner_ru', models.CharField(max_length=155, null=True, verbose_name='Заголовка баннера')),
                ('description_banner', models.CharField(max_length=155, verbose_name='Описание баннера')),
                ('description_banner_en', models.CharField(max_length=155, null=True, verbose_name='Описание баннера')),
                ('description_banner_ru', models.CharField(max_length=155, null=True, verbose_name='Описание баннера')),
                ('image_banner', models.ImageField(upload_to='background_images/', verbose_name='Изображение баннера')),
                ('image_banner_en', models.ImageField(null=True, upload_to='background_images/', verbose_name='Изображение баннера')),
                ('image_banner_ru', models.ImageField(null=True, upload_to='background_images/', verbose_name='Изображение баннера')),
                ('title_about', models.CharField(max_length=155, verbose_name='Заголовок')),
                ('title_about_en', models.CharField(max_length=155, null=True, verbose_name='Заголовок')),
                ('title_about_ru', models.CharField(max_length=155, null=True, verbose_name='Заголовок')),
                ('title_about2', models.CharField(max_length=155, verbose_name='Заголовок')),
                ('title_about2_en', models.CharField(max_length=155, null=True, verbose_name='Заголовок')),
                ('title_about2_ru', models.CharField(max_length=155, null=True, verbose_name='Заголовок')),
                ('title_about3', models.CharField(max_length=155, verbose_name='Заголовок')),
                ('title_about3_en', models.CharField(max_length=155, null=True, verbose_name='Заголовок')),
                ('title_about3_ru', models.CharField(max_length=155, null=True, verbose_name='Заголовок')),
                ('description_about', models.CharField(max_length=155, verbose_name='Описание баннера')),
                ('description_about_en', models.CharField(max_length=155, null=True, verbose_name='Описание баннера')),
                ('description_about_ru', models.CharField(max_length=155, null=True, verbose_name='Описание баннера')),
                ('description_about2', models.CharField(max_length=155, verbose_name='Заголовок')),
                ('description_about2_en', models.CharField(max_length=155, null=True, verbose_name='Заголовок')),
                ('description_about2_ru', models.CharField(max_length=155, null=True, verbose_name='Заголовок')),
                ('description_about3', models.CharField(max_length=155, verbose_name='Заголовок')),
                ('description_about3_en', models.CharField(max_length=155, null=True, verbose_name='Заголовок')),
                ('description_about3_ru', models.CharField(max_length=155, null=True, verbose_name='Заголовок')),
            ],
            options={
                'verbose_name': 'Настройка о нас',
                'verbose_name_plural': 'Настройки о нас',
            },
        ),
        migrations.AlterField(
            model_name='become',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='become/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='benefist',
            name='image',
            field=models.ImageField(upload_to='settings/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='cooking',
            name='image',
            field=models.ImageField(upload_to='settings/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='featured',
            name='image',
            field=models.ImageField(upload_to='settings/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='perfect',
            name='image',
            field=models.ImageField(upload_to='perfect/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='image',
            field=models.ImageField(upload_to='settings/', verbose_name='Фото'),
        ),
    ]
