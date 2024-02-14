from django.db import models

from apps.host.constant import BECOMEAHOST
from apps.base.models import Perfect


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