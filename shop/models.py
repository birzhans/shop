from django.db import models
from django.shortcuts import reverse

class Product(models.Model):
	title = models.CharField(max_length=150, db_index=True)
	slug = models.SlugField(max_length=150, unique=True)
	body = models.TextField(blank=True, unique=True)
	date_pub = models.DateTimeField(auto_now_add=True)
	photo = models.FileField(upload_to='media/')
	view_count=models.IntegerField(default=0)
	price = models.IntegerField(default=0)
	categories = models.ManyToManyField('Category', blank=True, related_name='products')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('product_detail_url', kwargs={'slug': self.slug})

	class Meta:
		ordering = ['-date_pub']


class Category(models.Model):
	title = models.CharField(max_length=150)
	slug = models.SlugField(max_length=150, blank=True, unique=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('category_detail_url', kwargs={'slug': self.slug})

	class Meta:
		ordering = ['title']

