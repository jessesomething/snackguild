from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.market_list, name='market_list'),
    url(r'^trader/(?P<fk>\w+)/$', views.trader_list, name='trader_list'),
    url(r'^market/(?P<pk>\d+)/$', views.trade_detail, name='trade_detail'),
    url(r'^market/new/$', views.trade_new, name='trade_new'),
    url(r'^market/(?P<fk>\w+)/(?P<cu>\w+)/trade/$', views.trade, name='trade'),
    url(r'^market/(?P<snack_id>\w+)/trade/$', views.update, name='update'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
]
