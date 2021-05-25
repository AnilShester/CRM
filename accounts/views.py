from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'accounts/home.html')
    
def about(request):
    my_dict = {'insert_me': " This is provided from the view function"}
    return render(request, 'accounts/products.html', context = my_dict)
    
def customer(request):
    return HttpResponse("Customer")