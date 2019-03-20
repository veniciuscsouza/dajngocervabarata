# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Basket(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    date_create = models.IntegerField()
    market_id = models.IntegerField()

    def __str__(self):
        return self.date_create


class Beers(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    brand_id = models.IntegerField()
    label = models.CharField(max_length=60)
    volume = models.IntegerField()
    def _str__(self):
        return self.label + ' ' + self.volume



class Brands(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    logo = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    descripton = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Markets(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    logo = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=60)

    def _str__(self):
        return self.name + ' ' + self.address


class Products(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    basket_id = models.IntegerField()
    markert_id = models.IntegerField()
    beer_id = models.IntegerField()
    price = models.FloatField()
    price_liter = models.FloatField()

    def __str__(self):
        return self.price_liter
