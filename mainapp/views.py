from django.shortcuts import render
from mainapp.models import Product,ProductCategory


def index(request):
    return render(request, 'mainapp/index.html')


def products(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    return render(request, 'mainapp/contact.html')
