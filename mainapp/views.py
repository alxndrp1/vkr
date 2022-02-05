from django.shortcuts import render
from .scripe import *
from .models import Univer

def index(request):
	if 'vuz' in request.GET:
		if request.GET['vuz'] == "2":
			univer = Univer.objects.get(id=2)
			vuz_inf(univer.orgsid_univer)
			vuz_inf_dict["Число публикаций на elibrary.ru"] = "<a target=\"_blank\" style=\" padding:0;\" class=\"btn btn-link\" href=\"https://elibrary.ru/org_items.asp?orgsid=14461&show_sotr=1&show_refs=0&show_option=1\">" + str(vuz_inf_dict["Число публикаций на elibrary.ru"]) + "</a>"
			vuz_inf_dict["Число публикаций в РИНЦ"] = "<a target=\"_blank\" style=\" padding:0;\" class=\"btn btn-link\" href=\"https://elibrary.ru/org_items.asp?orgsid=14461&show_sotr=1&show_refs=0&show_option=0\">" + str(vuz_inf_dict["Число публикаций в РИНЦ"]) + "</a>"
			vuz_inf_dict["Число публикаций, входящих в ядро РИНЦ"] = "<a target=\"_blank\" style=\" padding:0;\" class=\"btn btn-link\" href=\"https://elibrary.ru/org_items.asp?orgsid=14461&show_sotr=1&show_refs=0&show_option=2\">" + str(vuz_inf_dict["Число публикаций, входящих в ядро РИНЦ"]) + "</a>"
			return render(request, 'mainapp/index.html', {'univer' : univer, 'vuz_inf_dict' : vuz_inf_dict})
		if request.GET['vuz'] == "3":
			univer = Univer.objects.get(id=3)
			vuz_inf(univer.orgsid_univer)
			return render(request, 'mainapp/index.html', {'univer' : univer, 'vuz_inf_dict' : vuz_inf_dict})
		if request.GET['vuz'] == "4":
			univer = Univer.objects.get(id=4)
			vuz_inf(univer.orgsid_univer)
			return render(request, 'mainapp/index.html', {'univer' : univer, 'vuz_inf_dict' : vuz_inf_dict})
	return render(request, 'mainapp/index.html')
