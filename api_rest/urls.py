from api_rest import views
from django.urls import path

urlpatterns = [
    path('markets/', views.MarketsServiceView.as_view(), name='markets'),
    path('brands/', views.MarketsServiceView.as_view(), name='brands'),
    path('beers/', views.BeersListServiceView.as_view(), name='beers'),
    path('insertMarket/', views.InsertMarketServiceView.as_view(), name='insertMarket'),
    path('insertBrands/', views.insertBrandsServiceView.as_view(), name='insertBrands'),
    path('insertBeer/', views.InsertBeerServiceView.as_view(), name='insertBeer'),
]
