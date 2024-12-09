from multiprocessing import AuthenticationError
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render,redirect
from matplotlib import pyplot as plt
from matplotlib.style import context
from .forms import FavoriteCurrencyForm
from CurrencyConverter.settings import LOGIN_REDIRECT_URL
from .models import Currency, CurrencyRate, HistoricalRate, FavoriteCurrency
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from .forms import CurrencyConversionForm, CurrencyForm, FavoriteCurrencyForm
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from .models import FavoriteCurrency
from .forms import CurrencyForm
from django.contrib.auth import logout

# Create your views here

def home(request):
    return render(request, 'home.html')


# historical rates
def historical_rates(request, currency_code=None):
    if currency_code:
        # Logic when currency_code is provided
        rates = [{'date': '2024-12-01', 'rate': 100.25}]
    else:
        # Logic when currency_code is not provided
        rates = []

    context = {'currency_code': currency_code, 'rates': rates}
    return render(request, 'historical_rates.html', context)

#
    # multi_result
def multi_result(request):
    if request.method == "POST":
        from_currency = request.POST.get("from_currency")
        to_currencies = request.POST.getlist("to_currencies")
        amount = float(request.POST.get("amount"))

        from_rate = Currency.objects.get(code=from_currency).rate
        results = [
            {
                'to_currency': to_currency,
                'result': round((amount / from_rate) * Currency.objects.get(code=to_currency).rate, 2)
            }
            for to_currency in to_currencies
        ]

        return render(request, 'multi_result.html', {
            'results': results,
            'from_currency': from_currency,
            'amount': amount
        })

    currencies = Currency.objects.all()
    return render(request, 'multi_result.html', {'currencies': currencies})

# signing up page

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def currency_converter(request):
    return render(request, 'convert.html', context)

@login_required
def add_favorite(request):
    return redirect('favorites')

@login_required
def favorites(request):

    favorites = FavoriteCurrency.objects.filter(user=request.user)
    return render(request, 'favorites.html', {'favorites': favorites})

conversion_rates = {
    "USD": {"EUR": 0.91, "KES": 145.67, "GBP": 0.79, "INR": 83.22, "JPY": 150.14},
    "EUR": {"USD": 1.1, "KES": 160.23, "GBP": 0.87, "INR": 91.42, "JPY": 165.02},
    "KES": {"USD": 0.0069, "EUR": 0.0062, "GBP": 0.0054, "INR": 0.57, "JPY": 1.04},
}

# on favorites page
def favorites_page(request):
    if request.method == "POST":
        # Handle delete
        if 'delete' in request.POST:
            pair_to_delete = request.POST['delete']
            favorites = request.session.get('favorites', [])
            favorites = [pair for pair in favorites if f"{pair['from']} to {pair['to']}" != pair_to_delete]
            request.session['favorites'] = favorites
            request.session.modified = True
            return redirect('favorites')

        

def currency_register(request):
    if request.method == "POST":
        form = CurrencyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('convert_currency') 
    else:
        form = CurrencyForm()

    return render(request, 'currency_register.html', {'form': form})

#

def convert_currency(request):
    if request.method == 'POST':
        source_currency = request.POST.get('source_currency')
        target_currency = request.POST.get('target_currency')
        amount = float(request.POST.get('amount'))

        conversion_rates = {
            'USD': 1,
            'EUR': 0.92,
            'KES': 114.25,
            'GBP': 0.75,
            'INR': 83.50,
            'JPY': 147.60
        }

        if source_currency in conversion_rates and target_currency in conversion_rates:
            # Calculate the converted amount
            converted_amount = amount * conversion_rates[source_currency]
            converted_amount_to_target = converted_amount / conversion_rates[target_currency]
        else:
            converted_amount = converted_amount_to_target = None

        return render(request, 'convert.html', {
            'converted_amount': round(converted_amount, 2) if converted_amount else None,
            'converted_amount_to_target': round(converted_amount_to_target, 2) if converted_amount_to_target else None,
            'source_currency': source_currency,
            'target_currency': target_currency
        })
    
    return render(request, 'convert.html')

#for deleting and editing
def edit(request,id):
    currency = get_object_or_404(Currency, id=id)
    
    if request.method == 'POST':
        form = CurrencyConversionForm(request.POST,request.FILES,instance=currency)
        if form.is_valid():
            form.save()
            messages.success(request, 'Currency updated successfully!')
            return redirect('about')
        else:
            messages.error(request, 'Please check form details')
    else:
        form = CurrencyConversionForm(instance=currency)
    return render(request, 'edit.html',{'form':form,'currency':Currency})

def delete(request,id):
     currency = get_object_or_404(Currency, id=id)

     try:
         currency.delete()
         messages.success(request, 'Currency successfully deleted!')

     except Exception as e:
         messages.error(request, 'Currency not deleted')

     return redirect('convert')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = AuthenticationError(request, username=username, password=password)
        
        if user is not None:
            LOGIN_REDIRECT_URL(request, user)
            return redirect('/home') 
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login') 

#
  # Assuming this is the model that holds currency rates


def multi_result(request):
    conversion_results = []

    if request.method == 'POST':
        # Use get() to safely access the form data
        from_currency = request.POST.get('from_currency')
        to_currency = request.POST.get('to_currency')
        amount = request.POST.get('amount')

        # Ensure the form data is available before processing
        if from_currency and to_currency and amount:
            converted_amount = process_conversion(from_currency, to_currency, amount)
            conversion_results.append({
                'from_currency': from_currency,
                'to_currency': to_currency,
                'amount': amount,
                'converted_amount': converted_amount
            })
        else:
        
            conversion_results.append({
                'error': 'Please fill in all fields correctly.'
            })

    return render(request, 'multi_result.html', {
        'conversion_results': conversion_results,
    })
 



@login_required
def add_to_favorites(request):
    if request.method == "POST":
        form = FavoriteCurrencyForm(request.POST)
        if form.is_valid():
            currency = form.cleaned_data['currency']
            FavoriteCurrency.objects.create(user=request.user, currency=currency)
            return redirect('favorites')
    else:
        form = FavoriteCurrencyForm()

    currencies = Currency.objects.all()
    favorites = FavoriteCurrency.objects.filter(user=request.user)
    return render(request, 'favorites.html', {
        'form': form,
        'currencies': currencies,
        'favorites': favorites
    })

@login_required
def delete_favorite(request, favorite_id):
    try:
        favorite = FavoriteCurrency.objects.get(id=favorite_id, user=request.user)
        favorite.delete()
    except FavoriteCurrency.DoesNotExist:
        pass
    return redirect('favorites')




def process_conversion(from_currency, to_currency, amount):

    conversion_rates = {
        'USD': {'EUR': 0.85, 'GBP': 0.75},  
        'EUR': {'USD': 1.18, 'GBP': 0.88},  
        
    }
    
    # Convert the amount if valid rates exist
    if from_currency in conversion_rates and to_currency in conversion_rates[from_currency]:
        rate = conversion_rates[from_currency][to_currency]
        converted_amount = float(amount) * rate
        return converted_amount
    else:
        return 'Converted successfully'

#


import requests

def get_exchange_rate(from_currency, to_currency):
    url = f"https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest/{from_currency}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # Get the exchange rate for the target currency
        if 'conversion_rates' in data and to_currency in data['conversion_rates']:
            return data['conversion_rates'][to_currency]
        else:
            return None
    else:
        return None

def process_conversion(from_currency, to_currency, amount):
    # Fetch the conversion rate using the API
    rate = get_exchange_rate(from_currency, to_currency)

    if rate is None:
        return 'Rate not available'
    
    # Convert the amount
    converted_amount = float(amount) * rate
    return converted_amount

def multi_result(request):
    conversion_results = []

    if request.method == 'POST':
        from_currency = request.POST.get('from_currency')
        to_currency = request.POST.get('to_currency')
        amount = request.POST.get('amount')

        if from_currency and to_currency and amount:
            # Call the process conversion function
            converted_amount = process_conversion(from_currency, to_currency, amount)

            conversion_results.append({
                'from_currency': from_currency,
                'to_currency': to_currency,
                'amount': amount,
                'converted_amount': converted_amount
            })
        else:
            conversion_results.append({'error': 'Please fill in all fields correctly.'})

    return render(request, 'multi_result.html', {'conversion_results': conversion_results})



