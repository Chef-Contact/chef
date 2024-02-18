# Generated by Django 4.2.7 on 2024-02-14 17:16

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BecomeaHost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовок')),
                ('title_en', models.CharField(max_length=155, null=True, verbose_name='Заголовок')),
                ('title_ru', models.CharField(max_length=155, null=True, verbose_name='Заголовок')),
                ('descriptions', models.CharField(max_length=255, verbose_name='Описание')),
                ('descriptions_en', models.CharField(max_length=255, null=True, verbose_name='Описание')),
                ('descriptions_ru', models.CharField(max_length=255, null=True, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='becomeahost/', verbose_name='Фото')),
                ('image_en', models.ImageField(null=True, upload_to='becomeahost/', verbose_name='Фото')),
                ('image_ru', models.ImageField(null=True, upload_to='becomeahost/', verbose_name='Фото')),
                ('title2', models.CharField(max_length=155, verbose_name='Заголовок Выбора')),
                ('title2_en', models.CharField(max_length=155, null=True, verbose_name='Заголовок Выбора')),
                ('title2_ru', models.CharField(max_length=155, null=True, verbose_name='Заголовок Выбора')),
                ('title3', models.CharField(max_length=155, verbose_name='Заголовка ХОЗЯИН')),
                ('title3_en', models.CharField(max_length=155, null=True, verbose_name='Заголовка ХОЗЯИН')),
                ('title3_ru', models.CharField(max_length=155, null=True, verbose_name='Заголовка ХОЗЯИН')),
                ('title4', models.CharField(max_length=155, verbose_name='Заголовок Sing-in')),
                ('title4_en', models.CharField(max_length=155, null=True, verbose_name='Заголовок Sing-in')),
                ('title4_ru', models.CharField(max_length=155, null=True, verbose_name='Заголовок Sing-in')),
                ('descriptions2', models.CharField(max_length=255, verbose_name='Описание Sing-in')),
                ('descriptions2_en', models.CharField(max_length=255, null=True, verbose_name='Описание Sing-in')),
                ('descriptions2_ru', models.CharField(max_length=255, null=True, verbose_name='Описание Sing-in')),
                ('title5', models.CharField(max_length=155, verbose_name='заголовок reservation')),
                ('title5_en', models.CharField(max_length=155, null=True, verbose_name='заголовок reservation')),
                ('title5_ru', models.CharField(max_length=155, null=True, verbose_name='заголовок reservation')),
                ('descriptions3', models.CharField(max_length=255, verbose_name='Описание reservation')),
                ('descriptions3_en', models.CharField(max_length=255, null=True, verbose_name='Описание reservation')),
                ('descriptions3_ru', models.CharField(max_length=255, null=True, verbose_name='Описание reservation')),
                ('title6', models.CharField(max_length=155, verbose_name='Заголовок guests')),
                ('title6_en', models.CharField(max_length=155, null=True, verbose_name='Заголовок guests')),
                ('title6_ru', models.CharField(max_length=155, null=True, verbose_name='Заголовок guests')),
                ('descriptions4', models.CharField(max_length=255, verbose_name='Описание guests')),
                ('descriptions4_en', models.CharField(max_length=255, null=True, verbose_name='Описание guests')),
                ('descriptions4_ru', models.CharField(max_length=255, null=True, verbose_name='Описание guests')),
                ('title_end', models.CharField(max_length=155, verbose_name='Заголовка Chef ')),
                ('title_end_en', models.CharField(max_length=155, null=True, verbose_name='Заголовка Chef ')),
                ('title_end_ru', models.CharField(max_length=155, null=True, verbose_name='Заголовка Chef ')),
                ('image_end', models.ImageField(upload_to='becomeahost', verbose_name='Конечный фото')),
                ('image_end_en', models.ImageField(null=True, upload_to='becomeahost', verbose_name='Конечный фото')),
                ('image_end_ru', models.ImageField(null=True, upload_to='becomeahost', verbose_name='Конечный фото')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Настройки всего BecomeAHost',
            },
        ),
        migrations.CreateModel(
            name='BecomeEnd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовок')),
                ('title_en', models.CharField(max_length=155, null=True, verbose_name='Заголовок')),
                ('title_ru', models.CharField(max_length=155, null=True, verbose_name='Заголовок')),
                ('descritions', models.CharField(max_length=355, verbose_name='Описание')),
                ('descritions_en', models.CharField(max_length=355, null=True, verbose_name='Описание')),
                ('descritions_ru', models.CharField(max_length=355, null=True, verbose_name='Описание')),
                ('icon', models.CharField(choices=[('What does a publication include?', 'What does a publication include?'), ('Who can book my table?', 'Who can book my table?'), ('We’re here to help', 'We’re here to help'), ('Send messages to your guests', 'Send messages to your guests'), ('Organise a meeting after confirmation', 'Organise a meeting after confirmation'), ('Start with the essential', 'Start with the essential'), ('How do the guests pay?', 'How do the guests pay?'), ('How is done the wire-transfer to my account?', 'How is done the wire-transfer to my account?'), ('Homemeal fees', 'Homemeal fees'), ('How do I fix my fees?', 'How do I fix my fees?'), ('Homemeal insurance', 'Homemeal insurance'), ('Secured transactions', 'Secured transactions'), ('Trust and safety.', 'Trust and safety.'), ('So much more than money', 'So much more than money')], max_length=155, verbose_name='Иконка')),
                ('icon_en', models.CharField(choices=[('What does a publication include?', 'What does a publication include?'), ('Who can book my table?', 'Who can book my table?'), ('We’re here to help', 'We’re here to help'), ('Send messages to your guests', 'Send messages to your guests'), ('Organise a meeting after confirmation', 'Organise a meeting after confirmation'), ('Start with the essential', 'Start with the essential'), ('How do the guests pay?', 'How do the guests pay?'), ('How is done the wire-transfer to my account?', 'How is done the wire-transfer to my account?'), ('Homemeal fees', 'Homemeal fees'), ('How do I fix my fees?', 'How do I fix my fees?'), ('Homemeal insurance', 'Homemeal insurance'), ('Secured transactions', 'Secured transactions'), ('Trust and safety.', 'Trust and safety.'), ('So much more than money', 'So much more than money')], max_length=155, null=True, verbose_name='Иконка')),
                ('icon_ru', models.CharField(choices=[('What does a publication include?', 'What does a publication include?'), ('Who can book my table?', 'Who can book my table?'), ('We’re here to help', 'We’re here to help'), ('Send messages to your guests', 'Send messages to your guests'), ('Organise a meeting after confirmation', 'Organise a meeting after confirmation'), ('Start with the essential', 'Start with the essential'), ('How do the guests pay?', 'How do the guests pay?'), ('How is done the wire-transfer to my account?', 'How is done the wire-transfer to my account?'), ('Homemeal fees', 'Homemeal fees'), ('How do I fix my fees?', 'How do I fix my fees?'), ('Homemeal insurance', 'Homemeal insurance'), ('Secured transactions', 'Secured transactions'), ('Trust and safety.', 'Trust and safety.'), ('So much more than money', 'So much more than money')], max_length=155, null=True, verbose_name='Иконка')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Homemeal insurance',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовка')),
                ('title_en', models.CharField(max_length=155, null=True, verbose_name='Заголовка')),
                ('title_ru', models.CharField(max_length=155, null=True, verbose_name='Заголовка')),
                ('descriptions', models.CharField(max_length=255, verbose_name='Описание')),
                ('descriptions_en', models.CharField(max_length=255, null=True, verbose_name='Описание')),
                ('descriptions_ru', models.CharField(max_length=255, null=True, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='becomehost', verbose_name='Фото')),
                ('image_en', models.ImageField(null=True, upload_to='becomehost', verbose_name='Фото')),
                ('image_ru', models.ImageField(null=True, upload_to='becomehost', verbose_name='Фото')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Блог',
            },
        ),
        migrations.CreateModel(
            name='BlogActive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовка')),
                ('title_en', models.CharField(max_length=155, null=True, verbose_name='Заголовка')),
                ('title_ru', models.CharField(max_length=155, null=True, verbose_name='Заголовка')),
                ('descriptions', models.CharField(max_length=255, verbose_name='Описание')),
                ('descriptions_en', models.CharField(max_length=255, null=True, verbose_name='Описание')),
                ('descriptions_ru', models.CharField(max_length=255, null=True, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='becomehost', verbose_name='Фото')),
                ('image_en', models.ImageField(null=True, upload_to='becomehost', verbose_name='Фото')),
                ('image_ru', models.ImageField(null=True, upload_to='becomehost', verbose_name='Фото')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Блог active',
            },
        ),
        migrations.CreateModel(
            name='Free',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовок')),
                ('title_en', models.CharField(max_length=155, null=True, verbose_name='Заголовок')),
                ('title_ru', models.CharField(max_length=155, null=True, verbose_name='Заголовок')),
                ('descritions', models.CharField(max_length=355, verbose_name='Описание')),
                ('descritions_en', models.CharField(max_length=355, null=True, verbose_name='Описание')),
                ('descritions_ru', models.CharField(max_length=355, null=True, verbose_name='Описание')),
                ('icon', models.CharField(choices=[('What does a publication include?', 'What does a publication include?'), ('Who can book my table?', 'Who can book my table?'), ('We’re here to help', 'We’re here to help'), ('Send messages to your guests', 'Send messages to your guests'), ('Organise a meeting after confirmation', 'Organise a meeting after confirmation'), ('Start with the essential', 'Start with the essential'), ('How do the guests pay?', 'How do the guests pay?'), ('How is done the wire-transfer to my account?', 'How is done the wire-transfer to my account?'), ('Homemeal fees', 'Homemeal fees'), ('How do I fix my fees?', 'How do I fix my fees?'), ('Homemeal insurance', 'Homemeal insurance'), ('Secured transactions', 'Secured transactions'), ('Trust and safety.', 'Trust and safety.'), ('So much more than money', 'So much more than money')], max_length=155, verbose_name='Иконка')),
                ('icon_en', models.CharField(choices=[('What does a publication include?', 'What does a publication include?'), ('Who can book my table?', 'Who can book my table?'), ('We’re here to help', 'We’re here to help'), ('Send messages to your guests', 'Send messages to your guests'), ('Organise a meeting after confirmation', 'Organise a meeting after confirmation'), ('Start with the essential', 'Start with the essential'), ('How do the guests pay?', 'How do the guests pay?'), ('How is done the wire-transfer to my account?', 'How is done the wire-transfer to my account?'), ('Homemeal fees', 'Homemeal fees'), ('How do I fix my fees?', 'How do I fix my fees?'), ('Homemeal insurance', 'Homemeal insurance'), ('Secured transactions', 'Secured transactions'), ('Trust and safety.', 'Trust and safety.'), ('So much more than money', 'So much more than money')], max_length=155, null=True, verbose_name='Иконка')),
                ('icon_ru', models.CharField(choices=[('What does a publication include?', 'What does a publication include?'), ('Who can book my table?', 'Who can book my table?'), ('We’re here to help', 'We’re here to help'), ('Send messages to your guests', 'Send messages to your guests'), ('Organise a meeting after confirmation', 'Organise a meeting after confirmation'), ('Start with the essential', 'Start with the essential'), ('How do the guests pay?', 'How do the guests pay?'), ('How is done the wire-transfer to my account?', 'How is done the wire-transfer to my account?'), ('Homemeal fees', 'Homemeal fees'), ('How do I fix my fees?', 'How do I fix my fees?'), ('Homemeal insurance', 'Homemeal insurance'), ('Secured transactions', 'Secured transactions'), ('Trust and safety.', 'Trust and safety.'), ('So much more than money', 'So much more than money')], max_length=155, null=True, verbose_name='Иконка')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Sign-in for free',
            },
        ),
        migrations.CreateModel(
            name='Guests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовок')),
                ('title_en', models.CharField(max_length=155, null=True, verbose_name='Заголовок')),
                ('title_ru', models.CharField(max_length=155, null=True, verbose_name='Заголовок')),
                ('descritions', models.CharField(max_length=355, verbose_name='Описание')),
                ('descritions_en', models.CharField(max_length=355, null=True, verbose_name='Описание')),
                ('descritions_ru', models.CharField(max_length=355, null=True, verbose_name='Описание')),
                ('icon', models.CharField(choices=[('What does a publication include?', 'What does a publication include?'), ('Who can book my table?', 'Who can book my table?'), ('We’re here to help', 'We’re here to help'), ('Send messages to your guests', 'Send messages to your guests'), ('Organise a meeting after confirmation', 'Organise a meeting after confirmation'), ('Start with the essential', 'Start with the essential'), ('How do the guests pay?', 'How do the guests pay?'), ('How is done the wire-transfer to my account?', 'How is done the wire-transfer to my account?'), ('Homemeal fees', 'Homemeal fees'), ('How do I fix my fees?', 'How do I fix my fees?'), ('Homemeal insurance', 'Homemeal insurance'), ('Secured transactions', 'Secured transactions'), ('Trust and safety.', 'Trust and safety.'), ('So much more than money', 'So much more than money')], max_length=155, verbose_name='Иконка')),
                ('icon_en', models.CharField(choices=[('What does a publication include?', 'What does a publication include?'), ('Who can book my table?', 'Who can book my table?'), ('We’re here to help', 'We’re here to help'), ('Send messages to your guests', 'Send messages to your guests'), ('Organise a meeting after confirmation', 'Organise a meeting after confirmation'), ('Start with the essential', 'Start with the essential'), ('How do the guests pay?', 'How do the guests pay?'), ('How is done the wire-transfer to my account?', 'How is done the wire-transfer to my account?'), ('Homemeal fees', 'Homemeal fees'), ('How do I fix my fees?', 'How do I fix my fees?'), ('Homemeal insurance', 'Homemeal insurance'), ('Secured transactions', 'Secured transactions'), ('Trust and safety.', 'Trust and safety.'), ('So much more than money', 'So much more than money')], max_length=155, null=True, verbose_name='Иконка')),
                ('icon_ru', models.CharField(choices=[('What does a publication include?', 'What does a publication include?'), ('Who can book my table?', 'Who can book my table?'), ('We’re here to help', 'We’re here to help'), ('Send messages to your guests', 'Send messages to your guests'), ('Organise a meeting after confirmation', 'Organise a meeting after confirmation'), ('Start with the essential', 'Start with the essential'), ('How do the guests pay?', 'How do the guests pay?'), ('How is done the wire-transfer to my account?', 'How is done the wire-transfer to my account?'), ('Homemeal fees', 'Homemeal fees'), ('How do I fix my fees?', 'How do I fix my fees?'), ('Homemeal insurance', 'Homemeal insurance'), ('Secured transactions', 'Secured transactions'), ('Trust and safety.', 'Trust and safety.'), ('So much more than money', 'So much more than money')], max_length=155, null=True, verbose_name='Иконка')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Guests make a reservation',
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_descriptions', ckeditor.fields.RichTextField(verbose_name='Описание главной страницы')),
                ('button', models.CharField(max_length=155, verbose_name='Название кнопки (start)')),
                ('button_2', models.CharField(max_length=155, verbose_name='Название кнопки (next)')),
                ('button_3', models.CharField(max_length=155, verbose_name='Название кнопки (return)')),
                ('question_1', models.CharField(max_length=155, verbose_name='Тип услуги')),
                ('question_2', models.CharField(max_length=255, verbose_name='Тип кухни')),
                ('question_3', ckeditor.fields.RichTextField(verbose_name='Местоположение')),
                ('question_4', models.CharField(max_length=155, verbose_name='Дополнительные услуги')),
                ('question_5', models.CharField(max_length=155, verbose_name='Доставка заказа')),
                ('question_6', models.CharField(max_length=155, verbose_name='Соблюдение диеты')),
                ('question_7', models.CharField(max_length=155, verbose_name='Аллергены')),
                ('question_8', models.CharField(max_length=155, verbose_name='Гостей максимум')),
                ('question_9', models.CharField(max_length=155, verbose_name='Гостей минимум')),
                ('question_10', models.CharField(max_length=155, verbose_name='Сумма с гостей')),
                ('question_11', models.CharField(max_length=155, verbose_name='Дайте название вашему объявлению')),
                ('question_12', models.CharField(max_length=155, verbose_name='Напишите подробное описание объявления')),
                ('question_13', models.CharField(max_length=155, verbose_name='Добавьте фотографии в объявление')),
                ('question_14', ckeditor.fields.RichTextField(verbose_name='Описание о фотографии')),
                ('question_15', models.CharField(max_length=155, verbose_name='Укажите дату ')),
                ('question_16', ckeditor.fields.RichTextField(verbose_name='Условия установления даты')),
                ('question_17', ckeditor.fields.RichTextField(verbose_name='Страница Об условиях для гостей')),
                ('question_18', ckeditor.fields.RichTextField(verbose_name='Страница подтверждения данных')),
            ],
            options={
                'verbose_name_plural': 'Управление страницой  < стать шефом > ',
            },
        ),
        migrations.CreateModel(
            name='Receive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовок')),
                ('title_en', models.CharField(max_length=155, null=True, verbose_name='Заголовок')),
                ('title_ru', models.CharField(max_length=155, null=True, verbose_name='Заголовок')),
                ('descritions', models.CharField(max_length=355, verbose_name='Описание')),
                ('descritions_en', models.CharField(max_length=355, null=True, verbose_name='Описание')),
                ('descritions_ru', models.CharField(max_length=355, null=True, verbose_name='Описание')),
                ('icon', models.CharField(choices=[('What does a publication include?', 'What does a publication include?'), ('Who can book my table?', 'Who can book my table?'), ('We’re here to help', 'We’re here to help'), ('Send messages to your guests', 'Send messages to your guests'), ('Organise a meeting after confirmation', 'Organise a meeting after confirmation'), ('Start with the essential', 'Start with the essential'), ('How do the guests pay?', 'How do the guests pay?'), ('How is done the wire-transfer to my account?', 'How is done the wire-transfer to my account?'), ('Homemeal fees', 'Homemeal fees'), ('How do I fix my fees?', 'How do I fix my fees?'), ('Homemeal insurance', 'Homemeal insurance'), ('Secured transactions', 'Secured transactions'), ('Trust and safety.', 'Trust and safety.'), ('So much more than money', 'So much more than money')], max_length=155, verbose_name='Иконка')),
                ('icon_en', models.CharField(choices=[('What does a publication include?', 'What does a publication include?'), ('Who can book my table?', 'Who can book my table?'), ('We’re here to help', 'We’re here to help'), ('Send messages to your guests', 'Send messages to your guests'), ('Organise a meeting after confirmation', 'Organise a meeting after confirmation'), ('Start with the essential', 'Start with the essential'), ('How do the guests pay?', 'How do the guests pay?'), ('How is done the wire-transfer to my account?', 'How is done the wire-transfer to my account?'), ('Homemeal fees', 'Homemeal fees'), ('How do I fix my fees?', 'How do I fix my fees?'), ('Homemeal insurance', 'Homemeal insurance'), ('Secured transactions', 'Secured transactions'), ('Trust and safety.', 'Trust and safety.'), ('So much more than money', 'So much more than money')], max_length=155, null=True, verbose_name='Иконка')),
                ('icon_ru', models.CharField(choices=[('What does a publication include?', 'What does a publication include?'), ('Who can book my table?', 'Who can book my table?'), ('We’re here to help', 'We’re here to help'), ('Send messages to your guests', 'Send messages to your guests'), ('Organise a meeting after confirmation', 'Organise a meeting after confirmation'), ('Start with the essential', 'Start with the essential'), ('How do the guests pay?', 'How do the guests pay?'), ('How is done the wire-transfer to my account?', 'How is done the wire-transfer to my account?'), ('Homemeal fees', 'Homemeal fees'), ('How do I fix my fees?', 'How do I fix my fees?'), ('Homemeal insurance', 'Homemeal insurance'), ('Secured transactions', 'Secured transactions'), ('Trust and safety.', 'Trust and safety.'), ('So much more than money', 'So much more than money')], max_length=155, null=True, verbose_name='Иконка')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Receive your guests',
            },
        ),
        migrations.CreateModel(
            name='ChefRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_1', models.CharField(blank=True, max_length=155, null=True, verbose_name='Тип услуги')),
                ('question_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип кухни')),
                ('question_3', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Местоположение')),
                ('question_4', models.CharField(blank=True, max_length=155, null=True, verbose_name='Дополнительные услуги')),
                ('question_5', models.CharField(blank=True, max_length=155, null=True, verbose_name='Доставка заказа')),
                ('question_6', models.CharField(blank=True, max_length=155, null=True, verbose_name='Соблюдение диеты')),
                ('question_7', models.CharField(blank=True, max_length=155, null=True, verbose_name='Аллергены')),
                ('question_8', models.CharField(blank=True, max_length=155, null=True, verbose_name='Гостей максимум')),
                ('question_9', models.CharField(blank=True, max_length=155, null=True, verbose_name='Гостей минимум')),
                ('question_10', models.CharField(blank=True, max_length=155, null=True, verbose_name='Сумма с гостей')),
                ('question_11', models.CharField(blank=True, max_length=155, null=True, verbose_name='Дайте название вашему объявлению')),
                ('question_12', models.CharField(blank=True, max_length=155, null=True, verbose_name='Напишите подробное описание объявления')),
                ('image_host', models.ImageField(blank=True, null=True, upload_to='image_host/', verbose_name='фотография в объявлении')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chef_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Заявки на регистрацию шефа',
            },
        ),
    ]
