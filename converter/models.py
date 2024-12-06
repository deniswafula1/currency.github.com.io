from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#
class HistoricalRate(models.Model):
    code = models.CharField(max_length=3)
    date = models.DateField()
    rate = models.FloatField()

    def __str__(self):
        return f"{self.code} - {self.date}"



#



#
class CurrencyRate(models.Model):
    from_currency = models.CharField(max_length=3)
    to_currency = models.CharField(max_length=3)
    rate = models.DecimalField(max_digits=10, decimal_places=6)
    last_updated = models.DateTimeField(auto_now=True)

    

class Currency(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} ({self.code})"

class FavoriteCurrency(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s favorite {self.currency.name}"