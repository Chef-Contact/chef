# Generated by Django 4.2.7 on 2024-02-18 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0004_chefregister_image_host_en_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chefregister',
            options={'verbose_name_plural': 'Мерроприятия'},
        ),
        migrations.AlterModelOptions(
            name='host',
            options={'verbose_name_plural': 'Управление страницой  < создания меропрриятия > '},
        ),
    ]
