from django.db import models
from apps.users.models import User


class Category(models.Model):
    name = models.CharField(
        max_length = 55,
        verbose_name = 'Категория продукта'
    )

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Категория продукта'
        verbose_name_plural = 'Категории продукта'

class Kind(models.Model):
    name = models.CharField(
        max_length = 55,
        verbose_name = 'Кухня'
    )

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Кухня'
        verbose_name_plural = 'Кухня'


class Product(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название продукта'
    )
    description = models.TextField(
        verbose_name = 'Описание продукта'
    )
    image = models.ImageField(
        upload_to = 'product_images/',
        verbose_name = 'Фотография продукта'
    )
    price = models.IntegerField(
        verbose_name = 'Цена продукта'
    )
    delivery_price = models.IntegerField(
        verbose_name = 'Цена доставки'
    )
    calendar_availability_date = models.DateTimeField(
        verbose_name = 'Дата доступности продукта',
        null = True, blank = True
    )
    location = models.CharField(
        max_length = 255,
        null = True, blank = True,
        verbose_name = 'Локация продукта'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name = "products",
        limit_choices_to={'user_role': 'chef'},
        verbose_name = 'Пользователь'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name = 'products',
        null = True,
        verbose_name = 'Категория'
    )
    kind = models.ForeignKey(
        Kind,
        on_delete=models.SET_NULL,
        related_name = 'products',
        null = True,
        verbose_name = 'Тип кухни'
    )
    delivery_type = models.CharField(
        max_length = 55,
        verbose_name = 'Тип доставки'
    )

    def __str__(self):
        return f"{self.user.username}: {self.title} - {self.price}"
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class ProductImages(models.Model):
    product = models.ForeignKey(
        Product,
        verbose_name = 'images',
        on_delete = models.CASCADE
    )
    image = models.ImageField(
        upload_to='product_images/'
    )

    def __str__(self):
        return f"Доп фото продукта"
    
    class Meta:
        verbose_name = 'Доп фото продукта'
        verbose_name_plural = 'Доп фото продукта'
