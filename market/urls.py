from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.market_list, name='market_list')
]
