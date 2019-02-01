from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class News(models.Model):
    Id = models.IntegerField(primary_key=True)
    StockNews = models.TextField(blank=True)

    def __str__(self):
        return self.StockNews


class Stock(models.Model):
    StockName = models.CharField(blank=True, max_length=100)
    CurrentPrice = models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.StockName