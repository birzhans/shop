from django.db import models
from django.shortcuts import reverse
# Create your models here.


class Sale(models.Model):
	title = models.CharField(max_length=150, db_index=True)
	slug = models.SlugField(max_length=150, unique=True)
	body = models.TextField(blank=True, unique=True)
	date_pub = models.DateTimeField(auto_now_add=True)
	photo = models.FileField(upload_to='media/')
	view_count=models.IntegerField(default=0)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('sale_detail_url', kwargs={'slug': self.slug})

		

