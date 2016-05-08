from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Market, Trade_Cart
from .forms import TradeForm


def market_list(request):
    trades = Market.objects.filter(post_date__lte=timezone.now()).order_by('post_date')
    return render(request, 'market/market_list.html', {'trades' : trades})

def trade_detail(request, pk):
    trade = get_object_or_404(Market, pk=pk)
    return render(request, 'market/trade_detail.html', {'trade' : trade})

def trade(request, fk, cu):
    user = User.objects.get(username=fk)
    current_user = User.objects.get(username=cu)
    snacks = Market.objects.filter(Q(trader=current_user) | Q(trader=user))
    return render(request, 'market/trade.html', {'snacks' : snacks})

# def trade_cart(request, item, cu):
#     snack =


# def trader_list(request, uk):
#     traders = get_object_or_404(Market, pk=uk)
#     return render(request, 'market/trader_list.html', {'traders' : traders})

def trader_list(request, fk):
    user = User.objects.get(username=fk)
    current_user = request.user
    print(current_user)
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
def update(request, snack_id):
    snack = Market.objects.get(pk=snack_id)
    if snack.trading == False:
        snack.trading = True
        snack.save()
    elif snack.trading == True:
        snack.trading = False
        snack.save()
    return render(request, 'market/trade.html', {'snack' : snack})

@login_required
def trade_save(request):
    form = TradeForm()
    return render(request, 'market/trade_edit', {'form' : form})
