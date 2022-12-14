from django import views
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('executed/', views.saveParametros, name='executed'),
    path('sent/', views.sent, name='sent'),
    path('getData/', views.getData, name='getData'),
    path('getPage/', views.getPage, name='getPage'),
]