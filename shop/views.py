from django.shortcuts import render
from .models import *
# Create your views here.

def products_list(request):
	products = Product.objects.all()
	return render(request, 'shop/index.html', context={'products': products})


def product_detail(request, slug):
	product = Product.objects.get(slug__iexact=slug)
	product.view_count=product.view_count+1
	product.save()
	return render(request, 'shop/product_detail.html', context= {'product': product})


def category_detail(request, slug):
	category = Category.objects.get(slug__iexact=slug)
	return render(request, 'shop/category_detail.html', context= {'category': category})

def categories_list(request):
	categories = Category.objects.all()
	return render(request, 'shop/categories_list.html', context = {'categories':categories})