
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
                ('title_en', models.CharField(max_length=300, null=True, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=300, null=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Короткое описание')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Короткое описание')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Короткое описание')),
            ],
            options={
                'verbose_name': 'Часто задаваемый вопрос',
                'verbose_name_plural': 'Часто задаваемые вопросы',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300, verbose_name='вопрос')),
                ('question_en', models.CharField(max_length=300, null=True, verbose_name='вопрос')),
                ('question_ru', models.CharField(max_length=300, null=True, verbose_name='вопрос')),
                ('answer', models.TextField(verbose_name='ответ на вопрос')),
                ('answer_en', models.TextField(null=True, verbose_name='ответ на вопрос')),
                ('answer_ru', models.TextField(null=True, verbose_name='ответ на вопрос')),
                ('faq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faq', to='faq.faq', verbose_name='Часто задаваемый вопрос')),
            ],
            options={
                'verbose_name': 'Часто задаваемый вопрос',
                'verbose_name_plural': 'Часто задаваемые вопросы',
            },
        ),
    ]
