from django.contrib import admin
from converter.models import Currency, HistoricalRate

# Register your models here.
admin.site.register(Currency)
admin.site.register(HistoricalRate)
#admin.site.register(CurrencyRate)

