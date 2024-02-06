# Generated by Django 5.0.1 on 2024-02-06 21:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_work_forein_alter_work_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='benefist',
            name='forein',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.become'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cooking',
            name='forein',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.become'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='featured',
            name='forein',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.become'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perfect',
            name='forein',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.become'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='work_descriptions2',
            field=models.CharField(default=1, max_length=255, verbose_name='Описание - 2'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='benefist',
            name='title',
            field=models.CharField(max_length=155, verbose_name='Заголовка'),
        ),
        migrations.AlterField(
            model_name='cooking',
            name='title',
            field=models.CharField(max_length=155, verbose_name='Заголовка'),
        ),
        migrations.AlterField(
            model_name='featured',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовка'),
        ),
        migrations.AlterField(
            model_name='perfect',
            name='title',
            field=models.CharField(max_length=155, verbose_name='Заголовка'),
        ),
    ]