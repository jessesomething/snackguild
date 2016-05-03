from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Market
from .forms import TradeForm


def market_list(request):
    trades = Market.objects.filter(post_date__lte=timezone.now()).order_by('post_date')
    return render(request, 'market/market_list.html', {'trades' : trades})

def trade_detail(request, pk):
    trade = get_object_or_404(Market, pk=pk)
    return render(request, 'market/trade_detail.html', {'trade' : trade})

def trade(request, fk):
    user = User.objects.get(username=fk)
    traders = Market.objects.filter(trader=user)
    return render(request, 'market/trade.html', {'traders' : traders})

# def trader_list(request, uk):
#     traders = get_object_or_404(Market, pk=uk)
#     return render(request, 'market/trader_list.html', {'traders' : traders})

def trader_list(request, fk):
    user = User.objects.get(username=fk)
    traders = Market.objects.filter(trader=user)
    return render(request, 'market/trader_list.html', {'traders' : traders})

@login_required
def trade_new(request):
    if request.method == "POST":
        form = TradeForm(request.POST)
        if form.is_valid():
            trade = form.save(commit=False)
            trade.trader = request.user
            trade.post_date = timezone.now()
            trade.save()
            return redirect('trade_detail', pk=trade.pk)
    else:
        form = TradeForm()
    return render(request, 'market/trade_edit.html', {'form' : form})

@login_required
def trade_save(request):
    form = TradeForm()
    return render(request, 'market/trade_edit', {'form' : form})
