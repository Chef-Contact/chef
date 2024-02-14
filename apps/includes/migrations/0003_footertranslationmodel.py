# Generated by Django 4.2.7 on 2024-02-14 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('includes', '0002_headertranslationmodel_espace_home_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterTranslationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(max_length=50, verbose_name='Вкладка About')),
                ('about_en', models.CharField(max_length=50, null=True, verbose_name='Вкладка About')),
                ('about_ru', models.CharField(max_length=50, null=True, verbose_name='Вкладка About')),
                ('policies', models.CharField(max_length=50, verbose_name='Вкладка Policies')),
                ('policies_en', models.CharField(max_length=50, null=True, verbose_name='Вкладка Policies')),
                ('policies_ru', models.CharField(max_length=50, null=True, verbose_name='Вкладка Policies')),
                ('privacy', models.CharField(max_length=50, verbose_name='Вкладка Privacy')),
                ('privacy_en', models.CharField(max_length=50, null=True, verbose_name='Вкладка Privacy')),
                ('privacy_ru', models.CharField(max_length=50, null=True, verbose_name='Вкладка Privacy')),
                ('contests', models.CharField(max_length=50, verbose_name='Вкладка Contests')),
                ('contests_en', models.CharField(max_length=50, null=True, verbose_name='Вкладка Contests')),
                ('contests_ru', models.CharField(max_length=50, null=True, verbose_name='Вкладка Contests')),
                ('trustandsafety', models.CharField(max_length=50, verbose_name='Вкладка Trust And Safety')),
                ('trustandsafety_en', models.CharField(max_length=50, null=True, verbose_name='Вкладка Trust And Safety')),
                ('trustandsafety_ru', models.CharField(max_length=50, null=True, verbose_name='Вкладка Trust And Safety')),
                ('press', models.CharField(max_length=50, verbose_name='Вкладка Press')),
                ('press_en', models.CharField(max_length=50, null=True, verbose_name='Вкладка Press')),
                ('press_ru', models.CharField(max_length=50, null=True, verbose_name='Вкладка Press')),
                ('faq', models.CharField(max_length=50, verbose_name='Вкладка FAQ')),
                ('faq_en', models.CharField(max_length=50, null=True, verbose_name='Вкладка FAQ')),
                ('faq_ru', models.CharField(max_length=50, null=True, verbose_name='Вкладка FAQ')),
                ('contact_us', models.CharField(max_length=50, verbose_name='Вкладка Contact Us')),
                ('contact_us_en', models.CharField(max_length=50, null=True, verbose_name='Вкладка Contact Us')),
                ('contact_us_ru', models.CharField(max_length=50, null=True, verbose_name='Вкладка Contact Us')),
                ('howdoes', models.CharField(max_length=50, verbose_name='Вкладка How Does It Work')),
                ('howdoes_en', models.CharField(max_length=50, null=True, verbose_name='Вкладка How Does It Work')),
                ('howdoes_ru', models.CharField(max_length=50, null=True, verbose_name='Вкладка How Does It Work')),
                ('becomeahost', models.CharField(max_length=50, verbose_name='Вкладка Become a Host')),
                ('becomeahost_en', models.CharField(max_length=50, null=True, verbose_name='Вкладка Become a Host')),
                ('becomeahost_ru', models.CharField(max_length=50, null=True, verbose_name='Вкладка Become a Host')),
                ('hospitality', models.CharField(max_length=50, verbose_name='Вкладка Hospitality')),
                ('hospitality_en', models.CharField(max_length=50, null=True, verbose_name='Вкладка Hospitality')),
                ('hospitality_ru', models.CharField(max_length=50, null=True, verbose_name='Вкладка Hospitality')),
                ('specific_diets', models.CharField(max_length=50, verbose_name='Вкладка Specific Diets')),
                ('specific_diets_en', models.CharField(max_length=50, null=True, verbose_name='Вкладка Specific Diets')),
                ('specific_diets_ru', models.CharField(max_length=50, null=True, verbose_name='Вкладка Specific Diets')),
                ('explore', models.CharField(max_length=50, verbose_name='Вкладка Explore')),
                ('explore_en', models.CharField(max_length=50, null=True, verbose_name='Вкладка Explore')),
                ('explore_ru', models.CharField(max_length=50, null=True, verbose_name='Вкладка Explore')),
                ('host', models.CharField(max_length=50, verbose_name='Вкладка Host')),
                ('host_en', models.CharField(max_length=50, null=True, verbose_name='Вкладка Host')),
                ('host_ru', models.CharField(max_length=50, null=True, verbose_name='Вкладка Host')),
                ('social_media', models.CharField(max_length=50, verbose_name='Вкладка Social Media')),
                ('social_media_en', models.CharField(max_length=50, null=True, verbose_name='Вкладка Social Media')),
                ('social_media_ru', models.CharField(max_length=50, null=True, verbose_name='Вкладка Social Media')),
            ],
            options={
                'verbose_name': 'Кнопкa Footer',
                'verbose_name_plural': 'Кнопки Footer',
            },
        ),
    ]
