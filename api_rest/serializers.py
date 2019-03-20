from rest_framework import serializers
from cervas import models

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Markets
        fields = ('id', 'logo', 'name','address')
        depth = 1

class BrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brands
        fields = ('id', 'logo', 'name','descripton')
        depth = 1

class BeersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Beers
        fields = ('id', 'brand_id', 'label', 'volume')
        depth = 1
