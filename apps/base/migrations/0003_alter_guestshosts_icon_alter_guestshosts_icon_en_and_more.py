# Generated by Django 4.2.7 on 2024-02-18 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_perfectactive_context_price2_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestshosts',
            name='icon',
            field=models.CharField(choices=[('Find a publication', 'Find a publication'), ('Make a reservation with a host', 'Make a reservation with a host'), ('Go to your reservation', 'Go to your reservation'), ('Propose a meal', 'Propose a meal'), ('Handle your publications', 'Handle your publications'), ('Find a publication', 'Find a publication')], max_length=100, verbose_name='Иконка'),
        ),
        migrations.AlterField(
            model_name='guestshosts',
            name='icon_en',
            field=models.CharField(choices=[('Find a publication', 'Find a publication'), ('Make a reservation with a host', 'Make a reservation with a host'), ('Go to your reservation', 'Go to your reservation'), ('Propose a meal', 'Propose a meal'), ('Handle your publications', 'Handle your publications'), ('Find a publication', 'Find a publication')], max_length=100, null=True, verbose_name='Иконка'),
        ),
        migrations.AlterField(
            model_name='guestshosts',
            name='icon_ru',
            field=models.CharField(choices=[('Find a publication', 'Find a publication'), ('Make a reservation with a host', 'Make a reservation with a host'), ('Go to your reservation', 'Go to your reservation'), ('Propose a meal', 'Propose a meal'), ('Handle your publications', 'Handle your publications'), ('Find a publication', 'Find a publication')], max_length=100, null=True, verbose_name='Иконка'),
        ),
        migrations.AlterField(
            model_name='perfect',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='perfect/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='perfect',
            name='image_en',
            field=models.ImageField(blank=True, null=True, upload_to='perfect/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='perfect',
            name='image_ru',
            field=models.ImageField(blank=True, null=True, upload_to='perfect/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='perfect',
            name='title',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Заголовка'),
        ),
        migrations.AlterField(
            model_name='perfect',
            name='title_en',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Заголовка'),
        ),
        migrations.AlterField(
            model_name='perfect',
            name='title_ru',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Заголовка'),
        ),
        migrations.AlterField(
            model_name='perfectactive',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='perfect/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='perfectactive',
            name='image_en',
            field=models.ImageField(blank=True, null=True, upload_to='perfect/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='perfectactive',
            name='image_ru',
            field=models.ImageField(blank=True, null=True, upload_to='perfect/', verbose_name='Фото'),
        ),
    ]
