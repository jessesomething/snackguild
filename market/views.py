from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Market

def market_list(request):
    trades = Market.objects.filter(post_date__lte=timezone.now()).order_by('post_date')
    return render(request, 'market/market_list.html', {'trades' : trades})

def trade_detail(request, pk):
    trade = get_object_or_404(Market, pk=pk)
    return render(request, 'market/trade_detail.html', {'trade' : trade})
