from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.markets_list, name='market_list'),
]
