# Generated by Django 4.2.7 on 2024-02-11 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0002_free'),
    ]

    operations = [
        migrations.AddField(
            model_name='free',
            name='icon',
            field=models.CharField(choices=[('What does a publication include?', 'What does a publication include?'), ('Who can book my table?', 'Who can book my table?'), ('We’re here to help', 'We’re here to help'), ('Send messages to your guests', 'Send messages to your guests'), ('Organise a meeting after confirmation', 'Organise a meeting after confirmation'), ('Start with the essential', 'Start with the essential'), ('How do the guests pay?', 'How do the guests pay?'), ('How is done the wire-transfer to my account?', 'How is done the wire-transfer to my account?'), ('Homemeal fees', 'Homemeal fees'), ('How do I fix my fees?', 'How do I fix my fees?'), ('Homemeal insurance', 'Homemeal insurance'), ('Secured transactions', 'Secured transactions'), ('Trust and safety.', 'Trust and safety.'), ('So much more than money', 'So much more than money')], default=1, max_length=155, verbose_name='Иконка'),
            preserve_default=False,
        ),
    ]