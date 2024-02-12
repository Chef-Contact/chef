# Generated by Django 4.2.7 on 2024-02-11 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_becomeactive'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='becomeactive',
            options={'verbose_name': '', 'verbose_name_plural': 'Познакомьтесь с другими культурами Active'},
        ),
        migrations.RemoveField(
            model_name='becomeactive',
            name='parent_become',
        ),
        migrations.AddField(
            model_name='becomeactive',
            name='forein',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.become'),
            preserve_default=False,
        ),
    ]
