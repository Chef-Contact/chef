# Generated by Django 4.2.7 on 2024-02-10 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_insuranceobjects_trustsafety_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trustsafety',
            name='description',
        ),
        migrations.RemoveField(
            model_name='trustsafety',
            name='icon_image',
        ),
        migrations.RemoveField(
            model_name='trustsafety',
            name='title',
        ),
    ]