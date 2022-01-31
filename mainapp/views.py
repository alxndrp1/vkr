from django.shortcuts import render

from .models import Univer

def index(request):
	list_univer = Univer.objects.all()
	return render(request, 'index.html', {'list_univer' : list_univer})
