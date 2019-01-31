from django.shortcuts import render,redirect

from .models import *
from django.http import HttpResponse
# Create your views here.
def index(request):
	return render(request, 'posts/fullpage.html')

def news(request):
    news_list=News.objects.all()
    NewsDic={'news':news_list}
    return render(request,'posts/News.html',context=NewsDic)


def stockprice(request):
    stock_list=Stock.objects.all()
    StockDic={'stocks':stock_list}
    return render(request,'posts/stock.html',context=StockDic)
