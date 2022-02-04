from django.shortcuts import render
from .scripe import *
from .models import Univer

def index(request):
	if 'vuz' in request.GET:
		if request.GET['vuz'] == "1":
			univer = Univer.objects.get(id=2)
			obsh_chislo = vuz_inf(univer.orgsid_univer)
			return render(request, 'mainapp/index.html', {'univer' : univer, 'obsh_chislo' : obsh_chislo})
		if request.GET['vuz'] == "2":
			return render(request, 'mainapp/index.html', {'univer' : Univer.objects.get(id=3)})
		if request.GET['vuz'] == "3":
			return render(request, 'mainapp/index.html', {'univer' : Univer.objects.get(id=4)})
	return render(request, 'mainapp/index.html')
