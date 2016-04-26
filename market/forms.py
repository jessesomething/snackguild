from django import forms
from .models import Market

class TradeForm(forms.ModelForm):
    class Meta:
        model = Market
        fields = ('trader','snack','trade_type','snack_type','country','state')
