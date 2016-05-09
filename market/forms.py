from django import forms
from .models import Market, Trade_Cart

class TradeForm(forms.ModelForm):
    class Meta:
        model = Market
        fields = ('snack','trade_type','snack_type','country','state')

class CartForm(forms.ModelForm):
    class Meta:
        model = Trade_Cart
        fields = ('trader','snack','snack_type','country','state')

class TradeRequestForm(forms.ModelForm):
    class meta:
        model = Market
        fields = ('snack', 'snack_type')
