from django.db import models
from ckeditor.fields import RichTextField

from apps.host.constant import BECOMEAHOST
from apps.base.models import Perfect
from apps.users.models import User


# Create your models here.
class BecomeaHost(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    descriptions = models.CharField(
        max_length=255,
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='becomeahost/',
        verbose_name='Фото'
    )
    title2 = models.CharField(
        max_length=155,
        verbose_name='Заголовок Выбора'
    )
    title3 = models.CharField(
        max_length=155,
        verbose_name='Заголовка ХОЗЯИН'
    )
    title4 = models.CharField(
        max_length=155,
        verbose_name='Заголовок Sing-in'
    )
    descriptions2 = models.CharField(
        max_length=255,
        verbose_name='Описание Sing-in'
    )
    title5 = models.CharField(
        max_length=155,
        verbose_name='заголовок reservation'
    )
    descriptions3 = models.CharField(
        max_length=255,
        verbose_name='Описание reservation'
    )
    title6 = models.CharField(
        max_length=155,
        verbose_name='Заголовок guests'
    )
    descriptions4 = models.CharField(
        max_length=255,
        verbose_name='Описание guests'
    )
    title_end = models.CharField(
        max_length=155,
        verbose_name='Заголовка Chef '
    )
    image_end = models.ImageField(
        upload_to='becomeahost',
        verbose_name='Конечный фото'
    ) 

    def __str__(self):
        return self.title

    class Meta:
        verbose_name=''
        verbose_name_plural='Настройки всего BecomeAHost'



class Free(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name = 'Заголовок'
    )
    descritions = models.CharField(
        max_length=355,
        verbose_name ="Описание"
    )
    icon = models.CharField(
        choices=BECOMEAHOST,
        max_length=155,
        verbose_name = "Иконка"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ""
        verbose_name_plural = "Sign-in for free"


class Guests(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name = 'Заголовок'
    )
    descritions = models.CharField(
        max_length=355,
        verbose_name ="Описание"
    )
    icon = models.CharField(
        choices=BECOMEAHOST,
        max_length=155,
        verbose_name = "Иконка"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Guests make a reservation'


class Receive(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name = 'Заголовок'
    )
    descritions = models.CharField(
        max_length=355,
        verbose_name ="Описание"
    )
    icon = models.CharField(
        choices=BECOMEAHOST,
        max_length=155,
        verbose_name = "Иконка"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Receive your guests'

class BecomeEnd(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name = 'Заголовок'
    )
    descritions = models.CharField(
        max_length=355,
        verbose_name ="Описание" 
    )
    icon = models.CharField(
        choices=BECOMEAHOST,
        max_length=155,
        verbose_name = "Иконка"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Homemeal insurance'

class BlogActive(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name ='Заголовка'
    )
    descriptions = models.CharField(
        max_length=255,
        verbose_name = 'Описание'
    )
    image = models.ImageField(
        upload_to='becomehost',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Блог active'

class Blog(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name ='Заголовка'
    )
    descriptions = models.CharField(
        max_length=255,
        verbose_name = 'Описание'
    )
    image = models.ImageField(
        upload_to='becomehost',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Блог'


# -------------------asn--------------------------------------------

class Host(models.Model):
    title_descriptions = RichTextField(
        verbose_name="Описание главной страницы"
    )

    button = models.CharField(
        max_length= 155,
        verbose_name = 'Название кнопки (start)'
    )
    button_2 = models.CharField(
        max_length= 155,
        verbose_name = 'Название кнопки (next)'
    )
    button_3 = models.CharField(
        max_length= 155,
        verbose_name = 'Название кнопки (return)'
    )
    question_1 = models.CharField(
        max_length= 155,
        verbose_name = 'Тип услуги'
    )
    question_2 = models.CharField(
        max_length= 255,
        verbose_name = 'Тип кухни'
    )
    question_3 = RichTextField(
        verbose_name = 'Местоположение'
    )
    question_4 = models.CharField(
        max_length= 155,
        verbose_name = 'Дополнительные услуги'
    )
    question_5 = models.CharField(
        max_length= 155,
        verbose_name = 'Доставка заказа'
    )
    question_6 = models.CharField(
        max_length= 155,
        verbose_name = 'Соблюдение диеты'
    )
    question_7 = models.CharField(
        max_length= 155,
        verbose_name = 'Аллергены'
    )
    question_8 = models.CharField(
        max_length= 155,
        verbose_name = 'Гостей максимум'
    )
    question_9 = models.CharField(
        max_length= 155,
        verbose_name = 'Гостей минимум'
    )
    question_10 = models.CharField(
        max_length= 155,
        verbose_name = 'Сумма с гостей'
    )
    question_11 = models.CharField(
        max_length= 155,
        verbose_name = 'Дайте название вашему объявлению'
    )
    question_12 = models.CharField(
        max_length= 155,
        verbose_name = 'Напишите подробное описание объявления'
    )
    question_13 = models.CharField(
        max_length= 155,
        verbose_name = 'Добавьте фотографии в объявление'
    )
    question_14 = RichTextField(
        verbose_name = 'Описание о фотографии'
    )
    question_15 = models.CharField(
        max_length= 155,
        verbose_name = 'Укажите дату '
    )
    question_16 = RichTextField(
        verbose_name = 'Условия установления даты'
    )
    question_17 = RichTextField(
        verbose_name = 'Страница Об условиях для гостей'
    )
    question_18 = RichTextField(
        verbose_name = 'Страница подтверждения данных'
    )

    def __str__(self) -> str:
        return f"Страница создания меропрриятия шефа {self.id}"

    class Meta:
        verbose_name_plural = 'Управление страницой  < создания меропрриятия > '


class ChefRegister(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chef_user')
    question_1 = models.CharField(
        max_length= 155,
        blank=True, null=True,
        verbose_name = 'Тип услуги'
    )
    question_2 = models.CharField(
        max_length= 255,
        blank=True, null=True,
        verbose_name = 'Тип кухни'
    )
    question_3 = models.CharField(
        max_length= 255,
        blank=True, null=True,
        verbose_name = 'Местоположение'
    )
    question_4 = models.CharField(
        max_length= 155,
        blank=True, null=True,
        verbose_name = 'Дополнительные услуги'
    )
    question_5 = models.CharField(
        max_length= 155,
        blank=True, null=True,
        verbose_name = 'Доставка заказа'
    )
    question_6 = models.CharField(
        max_length= 155,
        blank=True, null=True,
        verbose_name = 'Соблюдение диеты'
    )
    question_7 = models.CharField(
        max_length= 155,
        blank=True, null=True,
        verbose_name = 'Аллергены'
    )
    question_8 = models.CharField(
        max_length= 155,
        blank=True, null=True,
        verbose_name = 'Гостей максимум'
    )
    question_9 = models.CharField(
        max_length= 155,
        blank=True, null=True,
        verbose_name = 'Гостей минимум'
    )
    question_10 = models.CharField(
        max_length= 155,
        blank=True, null=True,
        verbose_name = 'Сумма с гостей'
    )
    question_11 = models.CharField(
        max_length= 155,
        blank=True, null=True,
        verbose_name = 'Дайте название вашему объявлению'
    )
    question_12 = RichTextField(
        blank=True, null=True,
        verbose_name = 'Напишите подробное описание объявления'
    )
    image_host = models.ImageField(
        upload_to='image_host/',
        blank=True, null=True,
        verbose_name='фотография в объявлении'
    )
    

    def __str__(self) -> str:
        return f"Мерроприятие от шефа {self.user.username}"

    class Meta:
        verbose_name_plural = 'Мерроприятия'