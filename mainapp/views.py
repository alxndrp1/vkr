from django.shortcuts import render
from .scripe import *
from .models import Univer, Fakultet, Kafedra, Sotrud

def init_link(orgId):
	vuz_inf_dict["Число публикаций на elibrary.ru"] = "<a target=\"_blank\" style=\" padding:0;\" class=\"btn btn-link\" href=\"https://elibrary.ru/org_items.asp?orgsid=" + str(orgId) + "&show_sotr=1&show_refs=0&show_option=1\">" + str(vuz_inf_dict["Число публикаций на elibrary.ru"]) + "</a>"
	vuz_inf_dict["Число публикаций в РИНЦ"] = "<a target=\"_blank\" style=\" padding:0;\" class=\"btn btn-link\" href=\"https://elibrary.ru/org_items.asp?orgsid=" + str(orgId) + "&show_sotr=1&show_refs=0&show_option=0\">" + str(vuz_inf_dict["Число публикаций в РИНЦ"]) + "</a>"
	vuz_inf_dict["Число публикаций, входящих в ядро РИНЦ"] = "<a target=\"_blank\" style=\" padding:0;\" class=\"btn btn-link\" href=\"https://elibrary.ru/org_items.asp?orgsid=" + str(orgId) + "&show_sotr=1&show_refs=0&show_option=2\">" + str(vuz_inf_dict["Число публикаций, входящих в ядро РИНЦ"]) + "</a>"	

def index(request):
	if 'vuz' in request.GET:
		rej_view = 0
		if request.GET['vuz'] == "2":
			univer = Univer.objects.get(id=2)
			
			if 'sotrud' in request.GET:
				if int(request.GET['sotrud']) > 1:
					rej_view = 3
					sotr = Sotrud.objects.get(id=2)
					sotrud_inf(sotr.authorid_sotrud)
					sotrud = Sotrud.objects.all()
					return render(request, 'mainapp/index.html', {'sotr' : sotr, 'sotrud' : sotrud, 'sotrud_inf_dict' : sotrud_inf_dict, 'univer' : univer, 'vuz_inf_dict' : vuz_inf_dict, 'rej_view' : rej_view})
			
			sotrud = Sotrud.objects.all()
			vuz_inf(univer.orgsid_univer)
			init_link(univer.orgsid_univer)			
			return render(request, 'mainapp/index.html', {'univer' : univer, 'vuz_inf_dict' : vuz_inf_dict, 'sotrud' : sotrud, 'rej_view' : rej_view})

		if request.GET['vuz'] == "3":
			univer = Univer.objects.get(id=3)
			vuz_inf(univer.orgsid_univer)
			init_link(univer.orgsid_univer)
			return render(request, 'mainapp/index.html', {'univer' : univer, 'vuz_inf_dict' : vuz_inf_dict, 'rej_view' : rej_view})

		if request.GET['vuz'] == "4":
			univer = Univer.objects.get(id=4)
			vuz_inf(univer.orgsid_univer)
			init_link(univer.orgsid_univer)
			return render(request, 'mainapp/index.html', {'univer' : univer, 'vuz_inf_dict' : vuz_inf_dict, 'rej_view' : rej_view})
	return render(request, 'mainapp/index.html')
