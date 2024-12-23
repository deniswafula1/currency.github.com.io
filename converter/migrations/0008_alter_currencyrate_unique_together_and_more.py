# Generated by Django 5.0.7 on 2024-12-05 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0007_favoritecurrency_converted_amount_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='currencyrate',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='currencyrate',
            name='rate',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
    ]
