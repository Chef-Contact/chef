# Generated by Django 4.2.7 on 2024-02-10 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_trustsafety_insuranceobjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insuranceobjects',
            name='trustsafety',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insurance_trustsafety', to='base.trustsafety', verbose_name='Объект Insurance'),
        ),
        migrations.CreateModel(
            name='TrustSafetyObjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_image', models.ImageField(upload_to='icons/', verbose_name='Иконка элемента')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовок элемента')),
                ('description', models.TextField(verbose_name='Описание элемента')),
                ('trustsafety', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trust_trustsafety', to='base.trustsafety', verbose_name='Объект Trust')),
            ],
            options={
                'verbose_name': 'Доверие и Безопасность',
                'verbose_name_plural': 'Доверие и Безопасность',
            },
        ),
    ]
