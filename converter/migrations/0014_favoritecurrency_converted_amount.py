# Generated by Django 5.0.7 on 2024-12-06 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0013_currencyrate_last_updated_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='favoritecurrency',
            name='converted_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
