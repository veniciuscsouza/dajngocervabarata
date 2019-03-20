from django.shortcuts import render
from cervas import models
from api_rest import serializers
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class MarketsServiceView(generics.ListCreateAPIView):
    queryset = models.Markets.objects.all()
    serializer_class = serializers.MarketSerializer

class InsertMarketServiceView(APIView):

    def post(self, request, format=None):
        logo = request.data.get('logo')
        name = request.data.get('name')
        address = request.data.get('address')
        makert = models.Markets.objects.create(logo = logo, name = name, address = address)
        serializer = serializers.MarketSerializer(makert)
        return Response(serializer.data)

class BrandsServiceView(generics.ListCreateAPIView):
    queryset = models.Brands.objects.all()
    serializer_class = serializers.BrandsSerializer

class insertBrandsServiceView(APIView):

    def post(self, request, format=None):
        logo = request.data.get('logo')
        name = request.data.get('name')
        descripton = request.data.get('descripton')
        brand = models.Brands.objects.create(logo = logo, name = name, descripton = descripton)
        serializer = serializers.MarketSerializer(brand)
        return Response(serializer.data)

class BeersListServiceView(generics.ListCreateAPIView):
    queryset = models.Beers.objects.all()
    serializer_class = serializers.BeersSerializer

class InsertBeerServiceView(APIView):

    def post(self, request, format=None):
        id = request.data.get('id')
        brand_id = request.data.get('brand_id')
        label = request.data.get('label')
        volume = request.data.get('valume')
        beer = models.Beers.objects.create(id = id, brand_id = brand_id, label = label, volume = volume)
        serializer = serializers.BeersSerializer(beer)
        return Response(serializer.data)
