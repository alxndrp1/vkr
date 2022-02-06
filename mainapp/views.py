from django.shortcuts import render
from .scripe import *
from .models import Univer, Fakultet, Kafedra, Sotrud

def init_link_org(orgId):
	vuz_inf_dict["Число публикаций на elibrary.ru"] = "<a target=\"_blank\" style=\" padding:0;\" class=\"btn btn-link\" href=\"https://elibrary.ru/org_items.asp?orgsid=" + str(orgId) + "&show_sotr=1&show_refs=0&show_option=1\">" + str(vuz_inf_dict["Число публикаций на elibrary.ru"]) + "</a>"
	vuz_inf_dict["Число публикаций в РИНЦ"] = "<a target=\"_blank\" style=\" padding:0;\" class=\"btn btn-link\" href=\"https://elibrary.ru/org_items.asp?orgsid=" + str(orgId) + "&show_sotr=1&show_refs=0&show_option=0\">" + str(vuz_inf_dict["Число публикаций в РИНЦ"]) + "</a>"
	vuz_inf_dict["Число публикаций, входящих в ядро РИНЦ"] = "<a target=\"_blank\" style=\" padding:0;\" class=\"btn btn-link\" href=\"https://elibrary.ru/org_items.asp?orgsid=" + str(orgId) + "&show_sotr=1&show_refs=0&show_option=2\">" + str(vuz_inf_dict["Число публикаций, входящих в ядро РИНЦ"]) + "</a>"	

def init_link_sotr(authorId):
	sotrud_inf_dict["Число публикаций на elibrary.ru"] = "<a target=\"_blank\" style=\" padding:0;\" class=\"btn btn-link\" href=\"https://elibrary.ru/author_items.asp?authorid=" + str(authorId) + "&show_option=1&show_refs=1\">" + str(sotrud_inf_dict["Число публикаций на elibrary.ru"]) + "</a>"
	sotrud_inf_dict["Число публикаций в РИНЦ"] = "<a target=\"_blank\" style=\" padding:0;\" class=\"btn btn-link\" href=\"https://elibrary.ru/author_items.asp?authorid=" + str(authorId) + "&pubrole=100&show_option=0&show_refs=1\">" + str(sotrud_inf_dict["Число публикаций в РИНЦ"]) + "</a>"
	sotrud_inf_dict["Число публикаций, входящих в ядро РИНЦ"] = "<a target=\"_blank\" style=\" padding:0;\" class=\"btn btn-link\" href=\"https://elibrary.ru/author_items.asp?authorid=" + str(authorId) + "&pubrole=100&show_refs=1&show_option=2\">" + str(sotrud_inf_dict["Число публикаций, входящих в ядро РИНЦ"]) + "</a>"	
	sotrud_inf_dict["Число цитирований из публикаций на elibrary.ru"] = "<a target=\"_blank\" style=\" padding:0;\" class=\"btn btn-link\" href=\"https://elibrary.ru/author_refs.asp?authorid=" + str(authorId) + "&show_option=1&show_refs=1\">" + str(sotrud_inf_dict["Число цитирований из публикаций на elibrary.ru"]) + "</a>"
	sotrud_inf_dict["Число цитирований из публикаций, входящих в РИНЦ"] = "<a target=\"_blank\" style=\" padding:0;\" class=\"btn btn-link\" href=\"https://elibrary.ru/author_refs.asp?authorid=" + str(authorId) + "&show_option=0&show_refs=1&pubrole=100\">" + str(sotrud_inf_dict["Число цитирований из публикаций, входящих в РИНЦ"]) + "</a>"
	sotrud_inf_dict["Число цитирований из публикаций, входящих в ядро РИНЦ"] = "<a target=\"_blank\" style=\" padding:0;\" class=\"btn btn-link\" href=\"https://elibrary.ru/author_refs.asp?authorid=" + str(authorId) + "&show_option=2&show_refs=1&pubrole=100\">" + str(sotrud_inf_dict["Число цитирований из публикаций, входящих в ядро РИНЦ"]) + "</a>"

def index(request):
	if 'vuz' in request.GET:
		rej_view = 0
		if request.GET['vuz'] == "2":
			univer = Univer.objects.get(id=2)
			
			if 'sotrud' in request.GET:
				if int(request.GET['sotrud']) > 1:
					rej_view = 3
					sotr = Sotrud.objects.get(id=int(request.GET['sotrud']))
					sotrud_inf(sotr.authorid_sotrud)
					init_link_sotr(sotr.authorid_sotrud)
					sotrud = Sotrud.objects.all()					
					return render(request, 'mainapp/index.html', {'sotr' : sotr, 'sotrud' : sotrud, 'sotrud_inf_dict' : sotrud_inf_dict, 'univer' : univer, 'vuz_inf_dict' : vuz_inf_dict, 'rej_view' : rej_view})
			
			sotrud = Sotrud.objects.all()
			vuz_inf(univer.orgsid_univer)
			init_link_org(univer.orgsid_univer)			
			return render(request, 'mainapp/index.html', {'univer' : univer, 'vuz_inf_dict' : vuz_inf_dict, 'sotrud' : sotrud, 'vuz_inf_tematic_dict' : vuz_inf_tematic_dict, 'rej_view' : rej_view})

		if request.GET['vuz'] == "3":
			univer = Univer.objects.get(id=3)
			vuz_inf(univer.orgsid_univer)
			init_link_org(univer.orgsid_univer)
			return render(request, 'mainapp/index.html', {'univer' : univer, 'vuz_inf_dict' : vuz_inf_dict, 'vuz_inf_tematic_dict' : vuz_inf_tematic_dict, 'rej_view' : rej_view})

		if request.GET['vuz'] == "4":
			univer = Univer.objects.get(id=4)
			vuz_inf(univer.orgsid_univer)
			init_link_org(univer.orgsid_univer)
			return render(request, 'mainapp/index.html', {'univer' : univer, 'vuz_inf_dict' : vuz_inf_dict, 'vuz_inf_tematic_dict' : vuz_inf_tematic_dict, 'rej_view' : rej_view})
	return render(request, 'mainapp/index.html')
