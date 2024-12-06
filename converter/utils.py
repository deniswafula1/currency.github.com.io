import requests
from .models import Currency, HistoricalRate
from datetime import datetime, timedelta
import io
import base64
import matplotlib.pyplot as plt
from django.shortcuts import render
from django.http import HttpResponse

def update_rates():
    # Fetch current rates
    url = "https://open.er-api.com/v6/latest/USD"  
    response = requests.get(url)
    data = response.json()

    for code, rate in data['rates'].items():
        Currency.objects.update_or_create(
            code=code,
            defaults={'rate': rate, 'name': code}
        )
    # Fetch historical rates for the last 7 days
    base_url = "https://open.er-api.com/v6/history/USD"
    today = datetime.today()
    for i in range(1, 8):
        date = (today - timedelta(days=i)).strftime("%Y-%m-%d")
        historical_response = requests.get(f"{base_url}/{date}")
        historical_data = historical_response.json()

        for code, rate in historical_data['rates'].items():
            HistoricalRate.objects.update_or_create(
                code=code,
                date=date,
                defaults={'rate': rate}
            )
# Function to handle currency conversion logic
def convert_currency_logic(amount, from_currency, to_currency):

    exchange_rates = {
        "USD": {
            "EUR": 0.85,
            "GBP": 0.75,
            "INR": 75.0
        },
        "EUR": {
            "USD": 1.18,
            "GBP": 0.88,
            "INR": 88.0
        },
        "GBP": {
            "USD": 1.33,
            "EUR": 1.14,
            "INR": 105.0
        },
        "INR": {
            "USD": 0.013,
            "EUR": 0.012,
            "GBP": 0.0095
        }
    }

    # Handle invalid currencies or non-existent conversion paths
    if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        exchange_rate = exchange_rates[from_currency][to_currency]
        converted_amount = amount * exchange_rate
        return converted_amount
    else:
        raise ValueError("Currency conversion for this pair is not available")
#    
    
    
