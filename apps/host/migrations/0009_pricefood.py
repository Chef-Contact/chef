# Generated by Django 4.2.7 on 2024-02-12 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_benefist_color'),
        ('host', '0008_becomeahost_image_end'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_price', models.CharField(max_length=155, verbose_name='Заголовка цены')),
                ('context_price', models.CharField(max_length=155, verbose_name='Описание цены')),
                ('title_price2', models.CharField(max_length=155, verbose_name='Заголовка цены 2')),
                ('context_price2', models.CharField(max_length=155, verbose_name='Описание цены 2')),
                ('foreing', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.perfect')),
                ('perfect_active', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.perfectactive')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Прием пищи',
            },
        ),
    ]