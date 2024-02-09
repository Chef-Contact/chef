# Generated by Django 5.0.1 on 2024-02-06 19:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_become_settings_benefist_cooking_featured_perfect_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='perfect',
            options={'verbose_name': 'Найдите идеальную еду', 'verbose_name_plural': 'Найдите идеальную еду'},
        ),
        migrations.AlterModelOptions(
            name='work',
            options={'verbose_name': 'Как это работает', 'verbose_name_plural': 'Как это работает'},
        ),
        migrations.AddField(
            model_name='become',
            name='parent_become',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_become', to='base.become'),
        ),
        migrations.AlterField(
            model_name='perfect',
            name='title',
            field=models.ForeignKey(max_length=155, on_delete=django.db.models.deletion.CASCADE, to='base.become', verbose_name='Заголовка'),
        ),
    ]
