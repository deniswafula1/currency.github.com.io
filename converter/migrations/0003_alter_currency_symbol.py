# Generated by Django 5.1.3 on 2024-12-03 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0002_remove_currency_rate_remove_favoritecurrency_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='symbol',
            field=models.CharField(max_length=5),
        ),
    ]