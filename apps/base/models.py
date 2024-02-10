from django.db import models
from ckeditor.fields import RichTextField
from apps.base.contants import ICONS

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовка"
    )
    descriptions = models.CharField(
        max_length=155,
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to="settings",
        verbose_name="Фото"
    )
    become_title = models.CharField(
        max_length=155,
        verbose_name='Заголовка become '
    )
    become_descriptions = models.TextField(
        max_length=300,
        verbose_name='Описание  become'
    )
    find_title = models.CharField(
        max_length=155,
        verbose_name='Заголовка find'
    )
    find_descriptions = models.CharField(
        max_length=255,
        verbose_name='Описание find'
    )
    work_title = models.CharField(
        max_length=155,
        verbose_name='Заголовка work'
    )
    work_descriptions = models.CharField(
        max_length=255,
        verbose_name='Описание work'
    )
    download_title = models.CharField(
        max_length=155,
        verbose_name='Заголовка download'
    )
    download_descriptions = models.CharField(
        max_length=255,
        verbose_name='Описание download'
    )
    host_title = models.CharField(
        max_length=155,
        verbose_name="Заголовка host"
    )
    benefist_title = models.CharField(
        max_length=155,
        verbose_name='Заголовка benefist'
    )

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name=''
        verbose_name_plural="Настройки Главной страницы"


class Become(models.Model):
    parent_become = models.ForeignKey('self', on_delete=models.CASCADE, related_name='child_become', blank=True, null=True)
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка',
        blank=True, null=True
    )
    descriptions = models.CharField(
        max_length=255,
        verbose_name='Описание',
        blank=True, null=True
    )
    image = models.ImageField(
        upload_to='become',
        verbose_name='Фото',
        blank=True, null=True
    )

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name=""
        verbose_name_plural="Познакомьтесь с другими культурами "

class Perfect(models.Model):
    forein = models.ForeignKey(Become, on_delete=models.CASCADE )
    title = models.CharField(
          verbose_name='Заголовка', 
          max_length=155
          )
    image = models.ImageField(
        upload_to='perfect', 
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Найдите идеальную еду"
        verbose_name_plural = "Найдите идеальную еду"


class Work(models.Model):
    forein = models.ForeignKey(Become, on_delete=models.CASCADE )
    title = models.CharField( 
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = models.CharField(
        max_length=255, 
        verbose_name='Описание'
    )
    icon = models.CharField(
        choices=ICONS,
        max_length=100,
        verbose_name = "Иконку"
    )


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Как это работает"
        verbose_name_plural = "Как это работает"


class Featured(models.Model):
    forein = models.ForeignKey(Become, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовка'
    )
    image = models.ImageField(
        upload_to="settings",
        verbose_name='Фото'
    )
    locations = models.CharField(
        max_length=100,
        verbose_name='Локация'
    )

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name=''
        verbose_name_plural='Рекомендуемые хосты'



class Cooking(models.Model):
    forein = models.ForeignKey(Become, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = models.CharField(
        max_length=200,
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='settings',
        verbose_name='Фото'
    )

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name=''
        verbose_name_plural='ВСТРЕЧАТЬ НОВЫХ ЛЮДЕЙ'


class Benefist(models.Model):
    forein = models.ForeignKey(Become, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = models.CharField(
        max_length=200,
        verbose_name='Описание заголовка'
    )
    context = models.CharField(
        max_length=155,
        verbose_name='описание'
    )
    image = models.ImageField(
        upload_to='settings',
        verbose_name='Фото'
    )

    def __str__(self):
        return f"{self.title} - {self.context[:20]}"

    class Meta:
        verbose_name=''
        verbose_name_plural='Преимущества домашней еды'



###############################################
class Contact(models.Model):
    last_name = models.CharField(
        max_length=155,
        verbose_name='ФИО'
    )
    email = models.CharField(
        max_length=155,
        verbose_name="Адрес электронной почты"
    )
    number = models.CharField(
        max_length=75,
        verbose_name='Номер телефона'
    )
    message = models.CharField(
        max_length=355,
        verbose_name='Сообщение'
    )

    def __str__(self):
        return  self.last_name

    class Meta:
        verbose_name = ""
        verbose_name_plural='Контакты'



class Policies(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name="Заголовок"
    )
    descriptions = RichTextField(
        verbose_name = "Описание"
    )

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name=''
        verbose_name_plural='Политика'


class Privacy(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = RichTextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name=''
        verbose_name_plural='Конфедициально'