# Generated by Django 4.2.7 on 2024-02-17 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_main_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='день рождения'),
        ),
        migrations.AddField(
            model_name='user',
            name='month_of_birth',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='месяц рождения'),
        ),
        migrations.AddField(
            model_name='user',
            name='year_of_birth',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='год рождения'),
        ),
    ]