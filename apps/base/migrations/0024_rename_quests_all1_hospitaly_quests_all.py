# Generated by Django 4.2.7 on 2024-02-13 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0023_rename_quests_all_hospitaly_quests_all3_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospitaly',
            old_name='quests_all1',
            new_name='quests_all',
        ),
    ]
