# Generated by Django 4.2.7 on 2024-02-19 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chef_pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='shop_user', to=settings.AUTH_USER_MODEL),
        ),
    ]