from django.shortcuts import render
from django.utils import timezone
from .models import Market

def market_list(request):
    trades = Market.objects.filter(post_date__lte=timezone.now()).order_by('post_date')
    return render(request, 'market/market_list.html', {'trades' : trades})
