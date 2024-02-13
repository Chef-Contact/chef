# Generated by Django 4.2.7 on 2024-02-11 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_settings_work_context'),
    ]

    operations = [
        migrations.CreateModel(
            name='BecomeActive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=155, null=True, verbose_name='Заголовка')),
                ('descriptions', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='become', verbose_name='Фото')),
                ('parent_become', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_become', to='base.becomeactive')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Познакомьтесь с другими культурами ',
            },
        ),
    ]