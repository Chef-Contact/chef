# Generated by Django 4.2.7 on 2024-02-14 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='main_language',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Основной язык'),
        ),
    ]
