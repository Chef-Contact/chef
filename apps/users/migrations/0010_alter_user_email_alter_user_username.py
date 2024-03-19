# Generated by Django 4.2.7 on 2024-03-19 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, error_messages={'unique': 'Пользователь с таким email уже существует.'}, max_length=254, null=True, unique=True, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, error_messages={'unique': 'Пользователь с таким именем пользователя уже существует.'}, max_length=30, null=True, unique=True),
        ),
    ]
