# Generated by Django 4.2.7 on 2024-03-19 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_product_calendar_availability_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='calendar_availability_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата доступности продукта'),
        ),
    ]
