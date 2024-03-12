from django.db import models

# Create your models here.
class HeaderTranslationModel(models.Model):
    language_button = models.CharField(
        max_length = 50,
        verbose_name = 'Кнопка смены языка'
    )
    become_a_chef_button = models.CharField(
        max_length = 50,
        verbose_name = 'Кнопка "Стать шефом"'
    )
    sign_in = models.CharField(
        max_length = 50,
        verbose_name = 'Зарегистрироваться'
    )
    login = models.CharField(
        max_length = 50,
        verbose_name = 'Login'
    )
    messages = models.CharField(
        max_length = 50,
        verbose_name = 'Сообщения'
    )
    profile = models.CharField(
        max_length = 50,
        verbose_name = 'Профиль'
    )
    account_settings = models.CharField(
        max_length = 50,
        verbose_name = 'Настройки профиля'
    )
    logout = models.CharField(
        max_length = 50,
        verbose_name = ' "Logout"'
    )
    new_event = models.CharField(
        max_length = 50,
        verbose_name = 'Создание ивента'
    )
    events_in_progress = models.CharField(
        max_length = 50,
        verbose_name = 'Имеющиеся ивентов'
    )
    performances = models.CharField(
        max_length = 50,
        verbose_name = 'Блюда'
    )
    demands = models.CharField(
        max_length = 50,
        verbose_name = 'Demands'
    )
    payments_in = models.CharField(
        max_length = 50,
        verbose_name = 'Полученные платежи'
    )
    reservations = models.CharField(
        max_length = 50,
        verbose_name = 'Бронь'
    )
    payments_out = models.CharField(
        max_length = 50,
        verbose_name = 'Отправленные платежи'
    )
    espace_home = models.CharField(
        max_length = 50,
        verbose_name = 'Вкладка Espace'
    )

    def __str__(self):
        return self.language_button

    class Meta:
        verbose_name = 'Кнопка Header'
        verbose_name_plural = 'Кнопки Header'

class FooterTranslationModel(models.Model):
    about = models.CharField(
        max_length = 50,
        verbose_name = 'Вкладка About'
    )
    policies = models.CharField(
        max_length = 50,
        verbose_name = 'Вкладка Policies'
    )
    privacy = models.CharField(
        max_length = 50,
        verbose_name = 'Вкладка Privacy'
    )
    contests = models.CharField(
        max_length = 50,
        verbose_name = 'Вкладка Contests'
    )
    trustandsafety = models.CharField(
        max_length = 50,
        verbose_name = 'Вкладка Trust And Safety'
    )
    press = models.CharField(
        max_length = 50,
        verbose_name = 'Вкладка Press'
    )
    faq = models.CharField(
        max_length = 50,
        verbose_name = 'Вкладка FAQ'
    )
    contact_us = models.CharField(
        max_length = 50,
        verbose_name = 'Вкладка Contact Us'
    )
    howdoes = models.CharField(
        max_length = 50,
        verbose_name = 'Вкладка How Does It Work'
    )
    becomeahost = models.CharField(
        max_length = 50,
        verbose_name = 'Вкладка Become a Host'
    )
    hospitality = models.CharField(
        max_length = 50,
        verbose_name = 'Вкладка Hospitality'
    )
    specific_diets = models.CharField(
        max_length = 50,
        verbose_name = 'Вкладка Specific Diets'
    )
    explore = models.CharField(
        max_length = 50,
        verbose_name = 'Вкладка Explore'
    )
    host = models.CharField(
        max_length = 50,
        verbose_name = 'Вкладка Host'
    )
    social_media = models.CharField(
        max_length = 50,
        verbose_name = 'Вкладка Social Media'
    )

    class Meta:
        verbose_name = 'Кнопкa Footer'
        verbose_name_plural = 'Кнопки Footer'
