from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.market_list, name='market_list'),
    url(r'^market/(?P<pk>\d+)/$', views.trade_detail, name='trade_detail'),
]
