# Generated by Django 4.2.7 on 2024-02-11 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_become_descriptions_alter_become_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='work_context',
            field=models.CharField(default=1, max_length=255, verbose_name='Описание work'),
            preserve_default=False,
        ),
    ]
