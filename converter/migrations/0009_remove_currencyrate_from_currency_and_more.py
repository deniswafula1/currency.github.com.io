# Generated by Django 5.0.7 on 2024-12-05 09:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0008_alter_currencyrate_unique_together_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currencyrate',
            name='from_currency',
        ),
        migrations.RemoveField(
            model_name='currencyrate',
            name='to_currency',
        ),
        migrations.AddField(
            model_name='currencyrate',
            name='currency_code',
            field=models.CharField(default=1, max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='favoritecurrency',
            name='converted_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='favoritecurrency',
            name='from_currency',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='favoritecurrency',
            name='to_currency',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='favoritecurrency',
            name='user',
            field=models.ForeignKey(default=0.0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
