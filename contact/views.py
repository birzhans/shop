from django.shortcuts import render

# Create your views here.
from .forms import *

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = ContactForm()

	return render(request, 'contact/contact.html', {'form' : form})