# Generated by Django 4.2.7 on 2024-02-29 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chef_pages', '0005_shopdesign'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='tagline',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Слоган магазина'),
        ),
    ]
