from django.conf.urls import url
from django.urls import path,include
from . import views

app_name= 'posts'

urlpatterns = [
	path('', views.index,name='index'),
	path('News/', views.news, name="News"),
	path('stock/', views.stockprice, name="stockprice")

]