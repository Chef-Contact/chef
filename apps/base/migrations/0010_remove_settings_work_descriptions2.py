# Generated by Django 4.2.7 on 2024-02-06 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_settings_become_descriptions_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='work_descriptions2',
        ),
    ]