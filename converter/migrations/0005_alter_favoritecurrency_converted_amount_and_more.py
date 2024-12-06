# Generated by Django 5.1.3 on 2024-12-03 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0004_alter_currency_code_alter_currency_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritecurrency',
            name='converted_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='favoritecurrency',
            name='from_currency',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='favoritecurrency',
            name='to_currency',
            field=models.CharField(max_length=3),
        ),
    ]