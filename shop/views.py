from django.shortcuts import render
from .models import Product, Category, Order

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})

def order(request, id):
    product = Order.objects.filter(id=id)
    return render(request, 'shop/order.html', {'product': product})