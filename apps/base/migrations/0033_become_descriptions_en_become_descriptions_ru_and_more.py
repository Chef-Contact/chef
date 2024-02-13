# Generated by Django 4.2.7 on 2024-02-12 18:53

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0032_alter_cookingactive_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='become',
            name='descriptions_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='become',
            name='descriptions_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='become',
            name='image_en',
            field=models.ImageField(blank=True, null=True, upload_to='become/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='become',
            name='image_ru',
            field=models.ImageField(blank=True, null=True, upload_to='become/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='become',
            name='title_en',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Заголовка'),
        ),
        migrations.AddField(
            model_name='become',
            name='title_ru',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Заголовка'),
        ),
        migrations.AddField(
            model_name='becomeactive',
            name='descriptions_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='becomeactive',
            name='descriptions_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='becomeactive',
            name='image_en',
            field=models.ImageField(blank=True, null=True, upload_to='become', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='becomeactive',
            name='image_ru',
            field=models.ImageField(blank=True, null=True, upload_to='become', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='becomeactive',
            name='title_en',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Заголовка'),
        ),
        migrations.AddField(
            model_name='becomeactive',
            name='title_ru',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Заголовка'),
        ),
        migrations.AddField(
            model_name='benefist',
            name='color_en',
            field=models.CharField(choices=[('User-friendly', 'User-friendly'), ('Feel like home', 'Feel like home'), ('An insured quality', 'An insured quality'), ('Authenticity', 'Authenticity')], max_length=100, null=True, verbose_name='Цвет'),
        ),
        migrations.AddField(
            model_name='benefist',
            name='color_ru',
            field=models.CharField(choices=[('User-friendly', 'User-friendly'), ('Feel like home', 'Feel like home'), ('An insured quality', 'An insured quality'), ('Authenticity', 'Authenticity')], max_length=100, null=True, verbose_name='Цвет'),
        ),
        migrations.AddField(
            model_name='benefist',
            name='context_en',
            field=models.CharField(max_length=155, null=True, verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='benefist',
            name='context_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='benefist',
            name='descriptions_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Описание заголовка'),
        ),
        migrations.AddField(
            model_name='benefist',
            name='descriptions_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Описание заголовка'),
        ),
        migrations.AddField(
            model_name='benefist',
            name='image_en',
            field=models.ImageField(null=True, upload_to='settings/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='benefist',
            name='image_ru',
            field=models.ImageField(null=True, upload_to='settings/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='benefist',
            name='title_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка'),
        ),
        migrations.AddField(
            model_name='benefist',
            name='title_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка'),
        ),
        migrations.AddField(
            model_name='contact',
            name='email_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Адрес электронной почты'),
        ),
        migrations.AddField(
            model_name='contact',
            name='email_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Адрес электронной почты'),
        ),
        migrations.AddField(
            model_name='contact',
            name='last_name_en',
            field=models.CharField(max_length=155, null=True, verbose_name='ФИО'),
        ),
        migrations.AddField(
            model_name='contact',
            name='last_name_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='ФИО'),
        ),
        migrations.AddField(
            model_name='contact',
            name='message_en',
            field=models.CharField(max_length=355, null=True, verbose_name='Сообщение'),
        ),
        migrations.AddField(
            model_name='contact',
            name='message_ru',
            field=models.CharField(max_length=355, null=True, verbose_name='Сообщение'),
        ),
        migrations.AddField(
            model_name='contact',
            name='number_en',
            field=models.CharField(max_length=75, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='contact',
            name='number_ru',
            field=models.CharField(max_length=75, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='cooking',
            name='descriptions_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='cooking',
            name='descriptions_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='cooking',
            name='image_en',
            field=models.ImageField(null=True, upload_to='settings/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='cooking',
            name='image_ru',
            field=models.ImageField(null=True, upload_to='settings/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='cooking',
            name='title_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка'),
        ),
        migrations.AddField(
            model_name='cooking',
            name='title_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка'),
        ),
        migrations.AddField(
            model_name='cookingactive',
            name='descriptions_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='cookingactive',
            name='descriptions_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='cookingactive',
            name='image_en',
            field=models.ImageField(null=True, upload_to='settings/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='cookingactive',
            name='image_ru',
            field=models.ImageField(null=True, upload_to='settings/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='cookingactive',
            name='title_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка'),
        ),
        migrations.AddField(
            model_name='cookingactive',
            name='title_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка'),
        ),
        migrations.AddField(
            model_name='featured',
            name='image_en',
            field=models.ImageField(null=True, upload_to='settings/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='featured',
            name='image_ru',
            field=models.ImageField(null=True, upload_to='settings/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='featured',
            name='locations_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Локация'),
        ),
        migrations.AddField(
            model_name='featured',
            name='locations_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Локация'),
        ),
        migrations.AddField(
            model_name='featured',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовка'),
        ),
        migrations.AddField(
            model_name='featured',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовка'),
        ),
        migrations.AddField(
            model_name='insuranceobjects',
            name='answer_en',
            field=models.TextField(null=True, verbose_name='Ответ Insurance'),
        ),
        migrations.AddField(
            model_name='insuranceobjects',
            name='answer_ru',
            field=models.TextField(null=True, verbose_name='Ответ Insurance'),
        ),
        migrations.AddField(
            model_name='insuranceobjects',
            name='question_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Вопрос Insurance'),
        ),
        migrations.AddField(
            model_name='insuranceobjects',
            name='question_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Вопрос Insurance'),
        ),
        migrations.AddField(
            model_name='perfect',
            name='image_en',
            field=models.ImageField(null=True, upload_to='perfect/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='perfect',
            name='image_ru',
            field=models.ImageField(null=True, upload_to='perfect/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='perfect',
            name='title_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка'),
        ),
        migrations.AddField(
            model_name='perfect',
            name='title_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка'),
        ),
        migrations.AddField(
            model_name='perfectactive',
            name='image_en',
            field=models.ImageField(null=True, upload_to='perfect', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='perfectactive',
            name='image_ru',
            field=models.ImageField(null=True, upload_to='perfect', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='perfectactive',
            name='title_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка'),
        ),
        migrations.AddField(
            model_name='perfectactive',
            name='title_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка'),
        ),
        migrations.AddField(
            model_name='policies',
            name='descriptions_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='policies',
            name='descriptions_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='policies',
            name='title_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='policies',
            name='title_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='privacy',
            name='descriptions_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='privacy',
            name='descriptions_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='privacy',
            name='title_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка'),
        ),
        migrations.AddField(
            model_name='privacy',
            name='title_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка'),
        ),
        migrations.AddField(
            model_name='rules',
            name='description_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='rules',
            name='description_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='rules',
            name='flag1_en',
            field=models.ImageField(null=True, upload_to='flag_rules1/', verbose_name='Фото флага1'),
        ),
        migrations.AddField(
            model_name='rules',
            name='flag1_ru',
            field=models.ImageField(null=True, upload_to='flag_rules1/', verbose_name='Фото флага1'),
        ),
        migrations.AddField(
            model_name='rules',
            name='flag2_en',
            field=models.ImageField(null=True, upload_to='flag_rules2/', verbose_name='Фото флага2'),
        ),
        migrations.AddField(
            model_name='rules',
            name='flag2_ru',
            field=models.ImageField(null=True, upload_to='flag_rules2/', verbose_name='Фото флага2'),
        ),
        migrations.AddField(
            model_name='rules',
            name='image1_en',
            field=models.ImageField(null=True, upload_to='image_rules1/', verbose_name='Фотография 1'),
        ),
        migrations.AddField(
            model_name='rules',
            name='image1_ru',
            field=models.ImageField(null=True, upload_to='image_rules1/', verbose_name='Фотография 1'),
        ),
        migrations.AddField(
            model_name='rules',
            name='image2_en',
            field=models.ImageField(null=True, upload_to='image_rules2/', verbose_name='Фотография 2'),
        ),
        migrations.AddField(
            model_name='rules',
            name='image2_ru',
            field=models.ImageField(null=True, upload_to='image_rules2/', verbose_name='Фотография 2'),
        ),
        migrations.AddField(
            model_name='rules',
            name='lottery_rule_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Правило'),
        ),
        migrations.AddField(
            model_name='rules',
            name='lottery_rule_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Правило'),
        ),
        migrations.AddField(
            model_name='rules',
            name='main_image_en',
            field=models.ImageField(blank=True, null=True, upload_to='rules_image_main/', verbose_name='Главная фотография'),
        ),
        migrations.AddField(
            model_name='rules',
            name='main_image_ru',
            field=models.ImageField(blank=True, null=True, upload_to='rules_image_main/', verbose_name='Главная фотография'),
        ),
        migrations.AddField(
            model_name='rules',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='rules',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='settings',
            name='become_descriptions_en',
            field=models.TextField(max_length=300, null=True, verbose_name='Описание  become'),
        ),
        migrations.AddField(
            model_name='settings',
            name='become_descriptions_ru',
            field=models.TextField(max_length=300, null=True, verbose_name='Описание  become'),
        ),
        migrations.AddField(
            model_name='settings',
            name='become_title_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка become '),
        ),
        migrations.AddField(
            model_name='settings',
            name='become_title_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка become '),
        ),
        migrations.AddField(
            model_name='settings',
            name='benefist_title_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка benefist'),
        ),
        migrations.AddField(
            model_name='settings',
            name='benefist_title_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка benefist'),
        ),
        migrations.AddField(
            model_name='settings',
            name='descriptions_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='settings',
            name='descriptions_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='settings',
            name='download_descriptions_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Описание download'),
        ),
        migrations.AddField(
            model_name='settings',
            name='download_descriptions_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Описание download'),
        ),
        migrations.AddField(
            model_name='settings',
            name='download_title_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка download'),
        ),
        migrations.AddField(
            model_name='settings',
            name='download_title_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка download'),
        ),
        migrations.AddField(
            model_name='settings',
            name='find_descriptions_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Описание find'),
        ),
        migrations.AddField(
            model_name='settings',
            name='find_descriptions_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Описание find'),
        ),
        migrations.AddField(
            model_name='settings',
            name='find_title_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка find'),
        ),
        migrations.AddField(
            model_name='settings',
            name='find_title_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка find'),
        ),
        migrations.AddField(
            model_name='settings',
            name='host_title_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка host'),
        ),
        migrations.AddField(
            model_name='settings',
            name='host_title_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка host'),
        ),
        migrations.AddField(
            model_name='settings',
            name='image_en',
            field=models.ImageField(null=True, upload_to='settings/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='settings',
            name='image_ru',
            field=models.ImageField(null=True, upload_to='settings/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='settings',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовка'),
        ),
        migrations.AddField(
            model_name='settings',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовка'),
        ),
        migrations.AddField(
            model_name='settings',
            name='work_context_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Описание work - 2'),
        ),
        migrations.AddField(
            model_name='settings',
            name='work_context_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Описание work - 2'),
        ),
        migrations.AddField(
            model_name='settings',
            name='work_descriptions_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Описание work'),
        ),
        migrations.AddField(
            model_name='settings',
            name='work_descriptions_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Описание work'),
        ),
        migrations.AddField(
            model_name='settings',
            name='work_title_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка work'),
        ),
        migrations.AddField(
            model_name='settings',
            name='work_title_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка work'),
        ),
        migrations.AddField(
            model_name='trustsafety',
            name='background_image_en',
            field=models.ImageField(null=True, upload_to='background_images/', verbose_name='Изображение баннера'),
        ),
        migrations.AddField(
            model_name='trustsafety',
            name='background_image_ru',
            field=models.ImageField(null=True, upload_to='background_images/', verbose_name='Изображение баннера'),
        ),
        migrations.AddField(
            model_name='trustsafety',
            name='description_banner_en',
            field=models.TextField(null=True, verbose_name='Описание баннера'),
        ),
        migrations.AddField(
            model_name='trustsafety',
            name='description_banner_ru',
            field=models.TextField(null=True, verbose_name='Описание баннера'),
        ),
        migrations.AddField(
            model_name='trustsafety',
            name='insurance_description_en',
            field=models.TextField(null=True, verbose_name='Описание Insurance'),
        ),
        migrations.AddField(
            model_name='trustsafety',
            name='insurance_description_ru',
            field=models.TextField(null=True, verbose_name='Описание Insurance'),
        ),
        migrations.AddField(
            model_name='trustsafety',
            name='insurance_title_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовок Insurance'),
        ),
        migrations.AddField(
            model_name='trustsafety',
            name='insurance_title_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовок Insurance'),
        ),
        migrations.AddField(
            model_name='trustsafety',
            name='title_banner_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовок баннера'),
        ),
        migrations.AddField(
            model_name='trustsafety',
            name='title_banner_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовок баннера'),
        ),
        migrations.AddField(
            model_name='trustsafetyobjects',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание элемента'),
        ),
        migrations.AddField(
            model_name='trustsafetyobjects',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание элемента'),
        ),
        migrations.AddField(
            model_name='trustsafetyobjects',
            name='title_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовок элемента'),
        ),
        migrations.AddField(
            model_name='trustsafetyobjects',
            name='title_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовок элемента'),
        ),
        migrations.AddField(
            model_name='work',
            name='descriptions_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='work',
            name='descriptions_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='work',
            name='icon_en',
            field=models.CharField(choices=[('Find a table', 'Find a table '), ('Make a reservation', 'Make a reservation'), ('Go to the rendezvous', 'Go to the rendezvous')], max_length=100, null=True, verbose_name='Иконку'),
        ),
        migrations.AddField(
            model_name='work',
            name='icon_ru',
            field=models.CharField(choices=[('Find a table', 'Find a table '), ('Make a reservation', 'Make a reservation'), ('Go to the rendezvous', 'Go to the rendezvous')], max_length=100, null=True, verbose_name='Иконку'),
        ),
        migrations.AddField(
            model_name='work',
            name='title_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка'),
        ),
        migrations.AddField(
            model_name='work',
            name='title_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка'),
        ),
    ]
