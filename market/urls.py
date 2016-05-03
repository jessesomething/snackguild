from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.market_list, name='market_list'),
    # url(r'^trader/(?P<fk>\d+)/$', views.trader_list, name='trader_list'),
    url(r'^trader/(?P<fk>\w+)/$', views.trader_list, name='trader_list'),
    url(r'^market/(?P<pk>\d+)/$', views.trade_detail, name='trade_detail'),
    # url(r'^trader/(?P<uk>\d+)/$', views.trader_list, name='trader_list'),
    # url(r'^trader/$', views.trader_list, name='trader_list'),
    # url(r'^trader/(?P<fk>\d+)/$', views.trader_list, name='trader_list'),
    url(r'^market/new/$', views.trade_new, name='trade_new'),
    url(r'^market/(?P<fk>\w+)/trade/$', views.trade, name='trade'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
]
