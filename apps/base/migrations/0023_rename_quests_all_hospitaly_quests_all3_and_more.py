# Generated by Django 4.2.7 on 2024-02-13 00:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_alter_hospitaly_quests_all'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospitaly',
            old_name='quests_all',
            new_name='quests_all3',
        ),
        migrations.AddField(
            model_name='hospitaly',
            name='quests_all1',
            field=ckeditor.fields.RichTextField(default=1, verbose_name='Описание 2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospitaly',
            name='quests_all2',
            field=ckeditor.fields.RichTextField(default=1, verbose_name='Описание 3'),
            preserve_default=False,
        ),
    ]
