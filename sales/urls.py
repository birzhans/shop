from django.urls import path
from .views import *

urlpatterns = [
	path('', sales_list, name='sales_list_url'),
	path('popular/', popular, name='popular_items_url'),
	path('sales/<str:slug>/', sale_detail, name='sale_detail_url'),
]