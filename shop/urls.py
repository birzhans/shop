from django.urls import path
from .views import *

urlpatterns = [
	path('', products_list, name='products_list_url'),
	path('shop/<str:slug>/', product_detail, name='product_detail_url'),
	path('categories/', categories_list, name='categories_list_url'),
	path('categories/<slug>/', category_detail, name='category_detail_url'),
]