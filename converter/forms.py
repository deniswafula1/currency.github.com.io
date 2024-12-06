
from django import forms
from converter.models import Currency,HistoricalRate


# Form to take input for currency conversion
class CurrencyConversionForm(forms.Form):
    class Meta:
        model= Currency
        fields = '__all__'
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your code'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'rate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your rate'}),
        }
        
class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency 
        fields = ['name', 'code', 'symbol'] 
        
class FavoriteCurrencyForm(forms.Form):
    currency = forms.ModelChoiceField(queryset=Currency.objects.all(), required=True)

class HistoricalRate(forms.Form):
    class Meta:
        model= HistoricalRate
        model = Currency 
        fields = ['code', 'date', 'rate'] 
        