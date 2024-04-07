# Generated by Django 4.2.7 on 2024-04-05 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_productrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productrequest',
            name='add_service',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительные услуги'),
        ),
        migrations.AlterField(
            model_name='productrequest',
            name='color',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='productrequest',
            name='comment',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Комментарии по поводу заказа'),
        ),
        migrations.AlterField(
            model_name='productrequest',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='почта заказчика'),
        ),
        migrations.AlterField(
            model_name='productrequest',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ФИО заказчика'),
        ),
        migrations.AlterField(
            model_name='productrequest',
            name='number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер заказчика'),
        ),
    ]
