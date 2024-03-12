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
    steps = RichTextField(
        verbose_name="Шаги для клиента"
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
    question_3 = models.CharField(
        max_length= 155,
        verbose_name = 'Цена продукта'
    )
    question_4 = models.CharField(
        max_length= 155,
        verbose_name = 'Цена доставки'
    )
    question_5 = models.CharField(
        max_length= 155,
        verbose_name = 'Дайте название вашему продукту'
    )
    question_6 = models.CharField(
        max_length= 155,
        verbose_name = 'Напишите подробное описание продукта'
    )
    question_7 = models.CharField(
        max_length= 155,
        verbose_name = 'Добавьте фотографии продукта'
    )
    question_8 = models.TextField(
        verbose_name = 'Дополнительные фотографии продукта'
    )

    def __str__(self) -> str:
        return f"Страница создания меропрриятия шефа {self.id}"

    class Meta:
        verbose_name_plural = 'Управление страницой  < создания меропрриятия > '
