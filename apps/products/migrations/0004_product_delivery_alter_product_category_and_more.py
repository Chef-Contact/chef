# Generated by Django 4.2.7 on 2024-02-29 21:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_rename_peoductimages_productimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='delivery',
            field=models.CharField(default=1, max_length=55),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='products.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='kind',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='products.kind'),
        ),
        migrations.AlterField(
            model_name='product',
            name='user',
            field=models.ForeignKey(limit_choices_to={'user_role': 'chef'}, on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL),
        ),
    ]