# Generated by Django 4.2.7 on 2024-02-13 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0036_remove_settings_work_context_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestshosts',
            name='descriptions_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='guestshosts',
            name='descriptions_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='guestshosts',
            name='icon_en',
            field=models.CharField(choices=[('Find a publication', 'Find a publication'), ('Make a reservation with a host', 'Make a reservation with a host'), ('Go to your reservation', 'Go to your reservation'), ('Propose a meal', 'Propose a meal'), ('Handle your publications', 'Handle your publications'), ('Welcome your guests', 'Welcome your guests')], max_length=100, null=True, verbose_name='Иконка'),
        ),
        migrations.AddField(
            model_name='guestshosts',
            name='icon_ru',
            field=models.CharField(choices=[('Find a publication', 'Find a publication'), ('Make a reservation with a host', 'Make a reservation with a host'), ('Go to your reservation', 'Go to your reservation'), ('Propose a meal', 'Propose a meal'), ('Handle your publications', 'Handle your publications'), ('Welcome your guests', 'Welcome your guests')], max_length=100, null=True, verbose_name='Иконка'),
        ),
        migrations.AddField(
            model_name='guestshosts',
            name='title_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка'),
        ),
        migrations.AddField(
            model_name='guestshosts',
            name='title_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка'),
        ),
        migrations.AddField(
            model_name='howitworksobject',
            name='descriptions_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='howitworksobject',
            name='descriptions_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='howitworksobject',
            name='image_en',
            field=models.ImageField(null=True, upload_to='howitworks/'),
        ),
        migrations.AddField(
            model_name='howitworksobject',
            name='image_ru',
            field=models.ImageField(null=True, upload_to='howitworks/'),
        ),
        migrations.AddField(
            model_name='howitworksobject',
            name='title_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка'),
        ),
        migrations.AddField(
            model_name='howitworksobject',
            name='title_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Заголовка'),
        ),
    ]
