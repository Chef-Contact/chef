from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
import uuid

# Create your models here.
class User(AbstractUser):
    username = models.CharField(
        max_length=30,
        unique=True,
        default=None,
        help_text="Обязательное поле. Не более 30 символов. Только буквы, цифры и @/./+/-/_.",
        validators=[AbstractUser.username_validator],
        error_messages={
            'unique': "Пользователь с таким именем пользователя уже существует.",
        },
    )
    first_name = models.CharField(
        max_length=150,
        verbose_name="Имя",
        blank=True, null=True
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name="Фамилия",
        blank=True, null=True
    )
    profile_image = models.ImageField(
        upload_to = "profile_image/",
        verbose_name="Фотография профиля",
        blank = True, null = True,
        default = "profile_image/no_image.png"
    )
    biography = models.TextField(
        verbose_name="Биография",
        blank=True, null=True
    )
    phone = models.CharField(
        max_length=100,
        verbose_name="Номер телефона",
        blank=True, null=True
    )
    location = models.CharField(
        max_length=255,
        verbose_name='Адрес',
        blank=True, null=True
    )
    job = models.CharField(
        max_length=255,
        verbose_name='Работа',
        blank=True, null=True
    )
    main_language = models.CharField(
        max_length=255,
        verbose_name='Основной язык',
        blank=True, null=True
    )
    birthday = models.CharField(
        max_length=255,
        verbose_name='день рождения',
        blank=True, null=True
    )
    month_of_birth = models.CharField(
        max_length=255,
        verbose_name='месяц рождения',
        blank=True, null=True
    )
    year_of_birth = models.CharField(
        max_length=255,
        verbose_name='год рождения',
        blank=True, null=True
    )
    
    def save(self, *args, **kwargs):
        # Если значение username не установлено, генерировать значение по умолчанию
        if not self.username:
            base_username = f"user-{slugify(self.first_name)}-{slugify(self.last_name)}"[:25]
            self.username = f"{base_username}-{str(uuid.uuid4())[:4]}"

        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.username 
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        