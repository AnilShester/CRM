from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('products/', views.about, name = 'products'),
    path('customer/', views.customer, name = 'customer'),
]