# Generated by Django 4.2.7 on 2024-02-10 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_remove_settings_work_descriptions2'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='icon',
            field=models.CharField(choices=[('Find a table', 'Find a table '), ('Make a reservation', 'Make a reservation'), ('Go to the rendezvous', 'Go to the rendezvous')], default=1, max_length=100, verbose_name='Иконку'),
            preserve_default=False,
        ),
    ]