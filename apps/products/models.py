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
        null = True, blank = True,
        max_length = 255,
        verbose_name = 'Название продукта'
    )
    description = models.TextField(
        null = True, blank = True,
        verbose_name = 'Описание продукта'
    )
    image = models.ImageField(
        null = True, blank = True,
        upload_to = 'product_images/',
        verbose_name = 'Фотография продукта'
    )
    price = models.IntegerField(
        null = True, blank = True,
        verbose_name = 'Цена продукта'
    )
    price_per = models.CharField(
        null = True, blank = True,
        max_length = 255,
        verbose_name = 'Цена продукта за/'
    )
    delivery_price = models.IntegerField(
        null = True, blank = True,
        verbose_name = 'Цена доставки'
    )
    delivery_price_per = models.CharField(
        null = True, blank = True,
        max_length = 255,
        verbose_name = 'Цена доставки за/'
    )
    calendar_availability_date = models.DateField(
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
        null = True, blank = True,
        max_length = 55,
        verbose_name = 'Тип доставки'
    )
    diet = models.CharField(
        max_length = 55,
        null = True, blank = True,
        verbose_name = 'Диета'
    )
    allergens = models.CharField(
        max_length = 55,
        null = True, blank = True,
        verbose_name = 'Аллергены'
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


class ProductRequest(models.Model):
    chef = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name = "product_request_chef",
        verbose_name = 'Шеф'
    )
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name = "product_request_user",
        verbose_name = 'Пользователь (заказчик)'
    )
    product = models.ForeignKey(
        Product,
        verbose_name = 'Продукт',
        related_name = "product_request",
        on_delete = models.CASCADE
    )

    full_name = models.CharField(
        max_length=255,
        null = True, blank = True,
        verbose_name="ФИО заказчика"
    )
    email = models.EmailField(
        null = True, blank = True,
        verbose_name="почта заказчика"
    )
    number = models.CharField(
        max_length=255,
        null = True, blank = True,
        verbose_name="Номер заказчика"
    )

    color = models.CharField(
        max_length=255,
        null = True, blank = True,
        verbose_name="Цвет"
    )
    add_service = models.CharField(
        max_length=255,
        null = True, blank = True,
        verbose_name="Дополнительные услуги"
    )
    comment = models.CharField(
        max_length=255,
        null = True, blank = True,
        verbose_name="Комментарии по поводу заказа"
    )
    
    is_completed = models.BooleanField(
        default=False,
        verbose_name="Статус"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.customer.username} ---> {self.product}"
    
    class Meta:
        verbose_name = "История заказов"
        verbose_name_plural = "История заказов"