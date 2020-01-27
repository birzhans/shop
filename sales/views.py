from django.shortcuts import render
from .models import Sale

def sales_list(request):
	sales = Sale.objects.all()

	return render(request, 'sales/index.html' ,context = {'sales': sales})

def popular(request):
	return render(request, 'sales/popular.html')


def sale_detail(request, slug):
	sale = Sale.objects.get(slug__iexact=slug)
	sale.view_count=sale.view_count+1
	sale.save()
	return render(request, 'sales/sale_detail.html', context= {'sale': sale})

