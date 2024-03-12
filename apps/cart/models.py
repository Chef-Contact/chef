from django.db import models
from apps.products.models import Product
from apps.users.models import User
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(
        User,
        related_name = 'cart',
        on_delete = models.CASCADE,
        verbose_name = 'Владелец корзинки'
    )
    
    def __str__(self):
        return f"Корзинка пользователя: {self.user.username}"
    
    class Meta:
        verbose_name = 'Корзинка'
        verbose_name_plural = 'Корзинки'

class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        related_name = 'items',
        on_delete = models.CASCADE,
        verbose_name = 'Корзинка'
    )
    product = models.ForeignKey(
        Product,
        related_name = 'cart',
        on_delete = models.CASCADE,
        verbose_name = 'Продукт корзины'
    )
    count = models.IntegerField(
        verbose_name = 'Колличество продукта'
    )
    
    def __str__(self):
        return f"{self.product.title}-{self.cart.user.username} : {self.count}"
    
    class Meta:
        verbose_name = 'Продукт корзинки'
        verbose_name_plural = 'Продукты корзинки'