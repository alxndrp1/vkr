from django.shortcuts import render
from mainapp.models import Fakultet, Kafedra, Sotrud, Year, DateObn
from .scripe import *
from datetime import datetime

faks_list = []
kafs_list = []
sots_list = []

def index(request):
	kafn = 0
	
	if request.method == "POST":	
		for sot in Sotrud.objects.filter(kafedra=request.POST.get("kafn")):
			sot.otch_publ_rinc  = request.POST.get("sot_" + str(sot.id) + "_2_0")
			sot.otch_publ_yrinc = request.POST.get("sot_" + str(sot.id) + "_2_1")
			sot.otch_cit_rinc	= request.POST.get("sot_" + str(sot.id) + "_2_2")
			sot.otch_hir_rinc	= request.POST.get("sot_" + str(sot.id) + "_2_3")
			sot.elib_publ_rinc  = request.POST.get("sot_" + str(sot.id) + "_2_4")
			sot.elib_publ_yrinc = request.POST.get("sot_" + str(sot.id) + "_2_5")
			sot.elib_cit_rinc   = request.POST.get("sot_" + str(sot.id) + "_2_6")
			sot.elib_hir_rinc   = request.POST.get("sot_" + str(sot.id) + "_2_7")
			sot.save()
			try:
				year = Year.objects.get(sotrud=sot.id, year="2017")
			except Year.DoesNotExist:
				year = Year.objects.create(sotrud=sot, year="2017", elib_publ_rinc=0, elib_publ_yrinc=0, elib_cit_rinc=0, otch_publ_rinc=0, otch_publ_yrinc=0, otch_cit_rinc=0)
			year.otch_publ_rinc  = request.POST.get("sot_" + str(sot.id) + "_3_0")
			year.otch_publ_yrinc = request.POST.get("sot_" + str(sot.id) + "_3_1")
			year.otch_cit_rinc   = request.POST.get("sot_" + str(sot.id) + "_3_2")
			year.elib_publ_rinc  = request.POST.get("sot_" + str(sot.id) + "_3_4")
			year.elib_publ_yrinc = request.POST.get("sot_" + str(sot.id) + "_3_5")
			year.elib_cit_rinc   = request.POST.get("sot_" + str(sot.id) + "_3_6")
			year.save()
			try:
				year = Year.objects.get(sotrud=sot.id, year="2018")
			except Year.DoesNotExist:
				year = Year.objects.create(sotrud=sot, year="2018", elib_publ_rinc=0, elib_publ_yrinc=0, elib_cit_rinc=0, otch_publ_rinc=0, otch_publ_yrinc=0, otch_cit_rinc=0)
			year.otch_publ_rinc  = request.POST.get("sot_" + str(sot.id) + "_4_0")
			year.otch_publ_yrinc = request.POST.get("sot_" + str(sot.id) + "_4_1")
			year.otch_cit_rinc   = request.POST.get("sot_" + str(sot.id) + "_4_2")
			year.elib_publ_rinc  = request.POST.get("sot_" + str(sot.id) + "_4_4")
			year.elib_publ_yrinc = request.POST.get("sot_" + str(sot.id) + "_4_5")
			year.elib_cit_rinc   = request.POST.get("sot_" + str(sot.id) + "_4_6")
			year.save()
			try:
				year = Year.objects.get(sotrud=sot.id, year="2019")
			except Year.DoesNotExist:
				year = Year.objects.create(sotrud=sot, year="2019", elib_publ_rinc=0, elib_publ_yrinc=0, elib_cit_rinc=0, otch_publ_rinc=0, otch_publ_yrinc=0, otch_cit_rinc=0)
			year.otch_publ_rinc  = request.POST.get("sot_" + str(sot.id) + "_5_0")
			year.otch_publ_yrinc = request.POST.get("sot_" + str(sot.id) + "_5_1")
			year.otch_cit_rinc   = request.POST.get("sot_" + str(sot.id) + "_5_2")
			year.elib_publ_rinc  = request.POST.get("sot_" + str(sot.id) + "_5_4")
			year.elib_publ_yrinc = request.POST.get("sot_" + str(sot.id) + "_5_5")
			year.elib_cit_rinc   = request.POST.get("sot_" + str(sot.id) + "_5_6")
			year.save()
			try:
				year = Year.objects.get(sotrud=sot.id, year="2020")
			except Year.DoesNotExist:
				year = Year.objects.create(sotrud=sot, year="2020", elib_publ_rinc=0, elib_publ_yrinc=0, elib_cit_rinc=0, otch_publ_rinc=0, otch_publ_yrinc=0, otch_cit_rinc=0)
			year.otch_publ_rinc  = request.POST.get("sot_" + str(sot.id) + "_6_0")
			year.otch_publ_yrinc = request.POST.get("sot_" + str(sot.id) + "_6_1")
			year.otch_cit_rinc   = request.POST.get("sot_" + str(sot.id) + "_6_2")
			year.elib_publ_rinc  = request.POST.get("sot_" + str(sot.id) + "_6_4")
			year.elib_publ_yrinc = request.POST.get("sot_" + str(sot.id) + "_6_5")
			year.elib_cit_rinc   = request.POST.get("sot_" + str(sot.id) + "_6_6")
			year.save()
			try:
				year = Year.objects.get(sotrud=sot.id, year="2021")
			except Year.DoesNotExist:
				year = Year.objects.create(sotrud=sot, year="2021", elib_publ_rinc=0, elib_publ_yrinc=0, elib_cit_rinc=0, otch_publ_rinc=0, otch_publ_yrinc=0, otch_cit_rinc=0)
			year.otch_publ_rinc  = request.POST.get("sot_" + str(sot.id) + "_7_0")
			year.otch_publ_yrinc = request.POST.get("sot_" + str(sot.id) + "_7_1")
			year.otch_cit_rinc   = request.POST.get("sot_" + str(sot.id) + "_7_2")
			year.elib_publ_rinc  = request.POST.get("sot_" + str(sot.id) + "_7_4")
			year.elib_publ_yrinc = request.POST.get("sot_" + str(sot.id) + "_7_5")
			year.elib_cit_rinc   = request.POST.get("sot_" + str(sot.id) + "_7_6")
			year.save()
			try:
				year = Year.objects.get(sotrud=sot.id, year="2022")
			except Year.DoesNotExist:
				year = Year.objects.create(sotrud=sot, year="2022", elib_publ_rinc=0, elib_publ_yrinc=0, elib_cit_rinc=0, otch_publ_rinc=0, otch_publ_yrinc=0, otch_cit_rinc=0)
			year.otch_publ_rinc  = request.POST.get("sot_" + str(sot.id) + "_8_0")
			year.otch_publ_yrinc = request.POST.get("sot_" + str(sot.id) + "_8_1")
			year.otch_cit_rinc   = request.POST.get("sot_" + str(sot.id) + "_8_2")
			year.elib_publ_rinc  = request.POST.get("sot_" + str(sot.id) + "_8_4")
			year.elib_publ_yrinc = request.POST.get("sot_" + str(sot.id) + "_8_5")
			year.elib_cit_rinc   = request.POST.get("sot_" + str(sot.id) + "_8_6")
			year.save()			
		
		faks = Fakultet.objects.all()
		for fak in faks:
			faks_list.append([fak.id, fak.fakultet_name])		

		return render(request, 'registration/admin_panel.html', {"tab" : 1, "suc" : 1, "faks_list" : faks_list})
		
	else:
		if 'tab' in request.GET:
			if request.GET['tab'] == "1":
				faks_list.clear()
				kafs_list.clear()
				sots_list.clear()
				if 'fak' in request.GET:
					for kaf in Kafedra.objects.filter(fakultet=request.GET['fak']):
						kafs_list.append([kaf.id, kaf.kafedra_name])				

				if 'kaf' in request.GET:
					kafn = request.GET['kaf']
					for kaf in Kafedra.objects.filter(fakultet=Kafedra.objects.get(id=request.GET['kaf']).fakultet):
						kafs_list.append([kaf.id, kaf.kafedra_name])

					for sot in Sotrud.objects.filter(kafedra=request.GET['kaf']):
						sots_list.append([sot.id, sot.fio, [ 0,0,0,0, 0,0,0,0 ], [ 0,0,0, 0,0,0 ], [ 0,0,0, 0,0,0 ], [ 0,0,0, 0,0,0 ], [ 0,0,0, 0,0,0 ], [ 0,0,0, 0,0,0 ], [ 0,0,0, 0,0,0 ] ])
						sots_list[-1][2][0] = sot.otch_publ_rinc					
						sots_list[-1][2][1] = sot.otch_publ_yrinc 
						sots_list[-1][2][2] = sot.otch_cit_rinc
						sots_list[-1][2][3] = sot.otch_hir_rinc
						sots_list[-1][2][4] = sot.elib_publ_rinc					
						sots_list[-1][2][5] = sot.elib_publ_yrinc 
						sots_list[-1][2][6] = sot.elib_cit_rinc
						sots_list[-1][2][7] = sot.elib_hir_rinc

						try:
							if Year.objects.get(sotrud=sot.id, year = "2017"):
								year = Year.objects.get(sotrud=sot.id, year = "2017")
								sots_list[-1][3][0] = year.otch_publ_rinc
								sots_list[-1][3][1] = year.otch_publ_yrinc 
								sots_list[-1][3][2] = year.otch_cit_rinc
								sots_list[-1][3][3] = year.elib_publ_rinc
								sots_list[-1][3][4] = year.elib_publ_yrinc 
								sots_list[-1][3][5] = year.elib_cit_rinc
						except Year.DoesNotExist:
							pass

						try:
							if Year.objects.get(sotrud=sot.id, year = "2018"):
								year = Year.objects.get(sotrud=sot.id, year = "2018")
								sots_list[-1][4][0] = year.otch_publ_rinc
								sots_list[-1][4][1] = year.otch_publ_yrinc 
								sots_list[-1][4][2] = year.otch_cit_rinc
								sots_list[-1][4][3] = year.elib_publ_rinc
								sots_list[-1][4][4] = year.elib_publ_yrinc 
								sots_list[-1][4][5] = year.elib_cit_rinc
						except Year.DoesNotExist:
							pass

						try:
							if Year.objects.get(sotrud=sot.id, year = "2019"):
								year = Year.objects.get(sotrud=sot.id, year = "2019")
								sots_list[-1][5][0] = year.otch_publ_rinc
								sots_list[-1][5][1] = year.otch_publ_yrinc 
								sots_list[-1][5][2] = year.otch_cit_rinc
								sots_list[-1][5][3] = year.elib_publ_rinc
								sots_list[-1][5][4] = year.elib_publ_yrinc 
								sots_list[-1][5][5] = year.elib_cit_rinc
						except Year.DoesNotExist:
							pass

						try:
							if Year.objects.get(sotrud=sot.id, year = "2020"):
								year = Year.objects.get(sotrud=sot.id, year = "2020")
								sots_list[-1][6][0] = year.otch_publ_rinc
								sots_list[-1][6][1] = year.otch_publ_yrinc 
								sots_list[-1][6][2] = year.otch_cit_rinc
								sots_list[-1][6][3] = year.elib_publ_rinc
								sots_list[-1][6][4] = year.elib_publ_yrinc 
								sots_list[-1][6][5] = year.elib_cit_rinc
						except Year.DoesNotExist:
							pass

						try:
							if Year.objects.get(sotrud=sot.id, year = "2021"):
								year = Year.objects.get(sotrud=sot.id, year = "2021")
								sots_list[-1][7][0] = year.otch_publ_rinc
								sots_list[-1][7][1] = year.otch_publ_yrinc 
								sots_list[-1][7][2] = year.otch_cit_rinc
								sots_list[-1][7][3] = year.elib_publ_rinc
								sots_list[-1][7][4] = year.elib_publ_yrinc 
								sots_list[-1][7][5] = year.elib_cit_rinc
						except Year.DoesNotExist:
							pass					

						try:
							if Year.objects.get(sotrud=sot.id, year = "2022"):
								year = Year.objects.get(sotrud=sot.id, year = "2022")
								sots_list[-1][8][0] = year.otch_publ_rinc					
								sots_list[-1][8][1] = year.otch_publ_yrinc 
								sots_list[-1][8][2] = year.otch_cit_rinc
								sots_list[-1][8][3] = year.elib_publ_rinc
								sots_list[-1][8][4] = year.elib_publ_yrinc 
								sots_list[-1][8][5] = year.elib_cit_rinc
						except Year.DoesNotExist:
							pass				

				faks = Fakultet.objects.all()
				for fak in faks:
					faks_list.append([fak.id, fak.fakultet_name])

				return render(request, 'registration/admin_panel.html', {"tab" : 1, "faks_list" : faks_list, "kafs_list" : kafs_list, "sots_list" : sots_list, "kafn" : kafn})
		
		if 'obn' in request.GET:
			if request.GET['obn'] == "1":
				autoriz()
				for sot in Sotrud.objects.all():
					sotrud_inf( str(sot.authorid_sotrud) )
					sot.elib_publ_rinc  = sot_inf["publ_rinc"]
					sot.elib_publ_yrinc = sot_inf["publ_yrinc"]
					sot.elib_cit_rinc   = sot_inf["cit_rinc"]
					sot.elib_hir_rinc   = sot_inf["hir_rinc"]
					sot.save()									
					try:
						year = Year.objects.get(sotrud=sot.id, year="2017")
					except Year.DoesNotExist:
						year = Year.objects.create(sotrud=sot, year="2017", elib_publ_rinc=0, elib_publ_yrinc=0, elib_cit_rinc=0, otch_publ_rinc=0, otch_publ_yrinc=0, otch_cit_rinc=0)
					year.elib_publ_rinc  = sot_inf["2017_publ_rinc"]
					year.elib_publ_yrinc = sot_inf["2017_publ_yrinc"]
					year.elib_cit_rinc   = sot_inf["2017_cit_rinc"]
					year.save()
					try:
						year = Year.objects.get(sotrud=sot.id, year="2018")
					except Year.DoesNotExist:
						year = Year.objects.create(sotrud=sot, year="2018", elib_publ_rinc=0, elib_publ_yrinc=0, elib_cit_rinc=0, otch_publ_rinc=0, otch_publ_yrinc=0, otch_cit_rinc=0)
					year.elib_publ_rinc  = sot_inf["2018_publ_rinc"]
					year.elib_publ_yrinc = sot_inf["2018_publ_yrinc"]
					year.elib_cit_rinc   = sot_inf["2018_cit_rinc"]
					year.save()
					try:
						year = Year.objects.get(sotrud=sot.id, year="2019")
					except Year.DoesNotExist:
						year = Year.objects.create(sotrud=sot, year="2019", elib_publ_rinc=0, elib_publ_yrinc=0, elib_cit_rinc=0, otch_publ_rinc=0, otch_publ_yrinc=0, otch_cit_rinc=0)
					year.elib_publ_rinc  = sot_inf["2019_publ_rinc"]
					year.elib_publ_yrinc = sot_inf["2019_publ_yrinc"]
					year.elib_cit_rinc   = sot_inf["2019_cit_rinc"]
					year.save()
					try:
						year = Year.objects.get(sotrud=sot.id, year="2020")
					except Year.DoesNotExist:
						year = Year.objects.create(sotrud=sot, year="2020", elib_publ_rinc=0, elib_publ_yrinc=0, elib_cit_rinc=0, otch_publ_rinc=0, otch_publ_yrinc=0, otch_cit_rinc=0)
					year.elib_publ_rinc  = sot_inf["2020_publ_rinc"]
					year.elib_publ_yrinc = sot_inf["2020_publ_yrinc"]
					year.elib_cit_rinc   = sot_inf["2020_cit_rinc"]
					year.save()
					try:
						year = Year.objects.get(sotrud=sot.id, year="2021")
					except Year.DoesNotExist:
						year = Year.objects.create(sotrud=sot, year="2021", elib_publ_rinc=0, elib_publ_yrinc=0, elib_cit_rinc=0, otch_publ_rinc=0, otch_publ_yrinc=0, otch_cit_rinc=0)
					year.elib_publ_rinc  = sot_inf["2021_publ_rinc"]
					year.elib_publ_yrinc = sot_inf["2021_publ_yrinc"]
					year.elib_cit_rinc   = sot_inf["2021_cit_rinc"]
					year.save()
					try:
						year = Year.objects.get(sotrud=sot.id, year="2022")
					except Year.DoesNotExist:
						year = Year.objects.create(sotrud=sot, year="2022", elib_publ_rinc=0, elib_publ_yrinc=0, elib_cit_rinc=0, otch_publ_rinc=0, otch_publ_yrinc=0, otch_cit_rinc=0)
					year.elib_publ_rinc  = sot_inf["2022_publ_rinc"]
					year.elib_publ_yrinc = sot_inf["2022_publ_yrinc"]
					year.elib_cit_rinc   = sot_inf["2022_cit_rinc"]
					year.save()
					
					print("ФИО: " + sot.fio)
					print("Индекс Хирша: " + str(sot_inf["hir_rinc"]))
					print("Публикации в РИНЦ: " + str(sot_inf["publ_rinc"]))
					print("Цитирований в РИНЦ: " + str(sot_inf["cit_rinc"]))
					print("Публикаций в ядре РИНЦ: " + str(sot_inf["publ_yrinc"]))					

					print("Публикации в РИНЦ 2017г.: " + str(sot_inf["2017_publ_rinc"]))
					print("Цитирований в РИНЦ 2017г.: " + str(sot_inf["2017_cit_rinc"]))					
					print("Публикаций в ядре РИНЦ 2017г.: " + str(sot_inf["2017_publ_yrinc"]))

					print("Публикации в РИНЦ 2018г.: " + str(sot_inf["2018_publ_rinc"]))
					print("Цитирований в РИНЦ 2018г: " + str(sot_inf["2018_cit_rinc"]))
					print("Публикаций в ядре РИНЦ 2018г: " + str(sot_inf["2018_publ_yrinc"]))					

					print("Публикации в РИНЦ 2019г.: " + str(sot_inf["2019_publ_rinc"]))
					print("Цитирований в РИНЦ 2019г.: " + str(sot_inf["2019_cit_rinc"]))
					print("Публикаций в ядре РИНЦ 2019г.: " + str(sot_inf["2019_publ_yrinc"]))										

					print("Публикации в РИНЦ 2020г.: " + str(sot_inf["2020_publ_rinc"]))
					print("Цитирований в РИНЦ 2020г.: " + str(sot_inf["2020_cit_rinc"]))
					print("Публикаций в ядре РИНЦ 2020г.: " + str(sot_inf["2020_publ_yrinc"]))					

					print("Публикации в РИНЦ 2021г.: " + str(sot_inf["2021_publ_rinc"]))
					print("Цитирований в РИНЦ 2021г.: " + str(sot_inf["2021_cit_rinc"]))
					print("Публикаций в ядре РИНЦ 2021г.: " + str(sot_inf["2021_publ_yrinc"]))

					print("Публикации в РИНЦ 2022г.: " + str(sot_inf["2022_publ_rinc"]))
					print("Цитирований в РИНЦ 2022г.: " + str(sot_inf["2022_cit_rinc"]))
					print("Публикаций в ядре РИНЦ 2022г.: " + str(sot_inf["2022_publ_yrinc"]))
				dr_close()
				DateObn.objects.get(id=1).date_time = str(datetime.now())
				DateObn.objects.get(id=1).save()
	
	return render(request, 'registration/admin_panel.html', {"tab" : 0, "date_obn" : DateObn.objects.get(id=1).date_time})
