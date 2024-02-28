from django.db import models
from ckeditor.fields import RichTextField

from apps.users.models import User

# Create your models here.

class ShopDesign(models.Model):
    number = models.SmallIntegerField(
        verbose_name = 'Номер html документа',
    )
    image = models.ImageField(
        upload_to='design/',
        verbose_name="Фото дизайна",
    )
    full_image = models.ImageField(
        upload_to='design/',
        verbose_name='Полноё фото дизайна'
    )

    def __str__(self):
        return f"Дизайн {self.number}"
    
    class Meta:
        verbose_name = 'Дизайн'
        verbose_name_plural = 'Дизайны'

class Shop(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='shop_user')
    title = models.CharField(
        max_length=300,
        verbose_name="Название магазина",
        blank=True, null=True
    )
    back_image = models.ImageField(
        upload_to = "back_image/",
        verbose_name="Фото заднего фона на сайте",
        blank = True, null = True,
        default = "back_image/no_image.png"
    )
    location = models.CharField(
        max_length=300,
        verbose_name="Адрес",
        blank=True, null=True
    )
    description = RichTextField(
        verbose_name="Подробное описание о вас",
        blank=True, null=True
    )
    design = models.CharField(
        max_length=300,
        verbose_name="Дизайн профиля",
        blank=True, null=True
    )

    def __str__(self):
        return f"Дизайн магазина - {self.title} от пользователя {self.user.username}"
    
    class Meta:
        verbose_name = "Редактор дизайна профиля"
        verbose_name_plural = "Редактор дизайна профиля"