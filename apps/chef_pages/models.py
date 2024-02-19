from django.db import models

from apps.users.models import User

# Create your models here.

SHOP_DESIGN = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
)

class Shop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shop_user')
    title = models.CharField(
        max_length=300,
        verbose_name="Название магазина",
        blank=True, null=True
    )
    back_image = models.ImageField(
        upload_to = "back_image/",
        verbose_name="Фотография профиля",
        blank = True, null = True,
        default = "back_image/no_image.png"
    )
    location = models.CharField(
        max_length=300,
        verbose_name="Адрес",
        blank=True, null=True
    )
    description = models.TextField(
        verbose_name="Подробное описание о вас",
        blank=True, null=True
    )
    design = models.CharField(
        max_length=300,
        choices="we",
        verbose_name="Дизайн профиля",
        blank=True, null=True
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Часто задаваемый вопрос"
        verbose_name_plural = "Часто задаваемые вопросы"