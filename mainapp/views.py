from django.shortcuts import render
from .models import Fakultet, Kafedra, Sotrud, Year, DateObn
from django.db.models import Sum

use_fak_sname = ""
use_kaf_sname = ""
faks_list = []
kafs_list = []
sots_list = []
maxpok = 0

def calc_maxpok(pok):
	global maxpok
	if pok > maxpok:
		maxpok = pok

def set_kaf(_publ, _year, _kaf):
	global use_fak_sname, use_kaf_sname, maxpok
	maxpok = 0
	sots_list.clear()	
	use_fak_sname = Fakultet.objects.get(id=Kafedra.objects.get(id=_kaf).fakultet.id).fakultet_sname
	use_kaf_sname = Kafedra.objects.get(id=_kaf).kafedra_sname	
	if _year:
		for sot in Sotrud.objects.filter(kafedra=_kaf):
			sots_list.append([sot.fio_s, sot.fio, 0, 0, sot.authorid_sotrud, sot.kafedra.fakultet.id])
			if _publ == 0:
				try:
					sots_list[-1][2] += Year.objects.get(sotrud=sot.id, year = _year).otch_publ_rinc
					sots_list[-1][3] += Year.objects.get(sotrud=sot.id, year = _year).elib_publ_rinc
					calc_maxpok(sots_list[-1][2])
					calc_maxpok(sots_list[-1][3])
				except Year.DoesNotExist:
					sots_list[-1][2] += 0
					sots_list[-1][3] += 0
			elif _publ == 1:	
				try:
					sots_list[-1][2] += Year.objects.get(sotrud=sot.id, year = _year).otch_publ_yrinc
					sots_list[-1][3] += Year.objects.get(sotrud=sot.id, year = _year).elib_publ_yrinc
					calc_maxpok(sots_list[-1][2])
					calc_maxpok(sots_list[-1][3])					
				except Year.DoesNotExist:
					sots_list[-1][2] += 0
					sots_list[-1][3] += 0				
			elif _publ == 2:
				try:
					sots_list[-1][2] += Year.objects.get(sotrud=sot.id, year = _year).otch_cit_rinc
					sots_list[-1][3] += Year.objects.get(sotrud=sot.id, year = _year).elib_cit_rinc
					calc_maxpok(sots_list[-1][2])
					calc_maxpok(sots_list[-1][3])					
				except Year.DoesNotExist:
					sots_list[-1][2] += 0
					sots_list[-1][3] += 0
			elif _publ == 3:
				sots_list[-1][2] += sot.otch_hir_rinc
				sots_list[-1][3] += sot.elib_hir_rinc
				calc_maxpok(sots_list[-1][2])
				calc_maxpok(sots_list[-1][3])				
	else:		
		for sot in Sotrud.objects.filter(kafedra=_kaf):
			sots_list.append([sot.fio_s, sot.fio, 0, 0, sot.authorid_sotrud, sot.kafedra.fakultet.id])
			if _publ == 0:
				sots_list[-1][2] += sot.otch_publ_rinc
				sots_list[-1][3] += sot.elib_publ_rinc
				calc_maxpok(sots_list[-1][2])
				calc_maxpok(sots_list[-1][3])				
			elif _publ == 1:	
				sots_list[-1][2] += sot.otch_publ_yrinc
				sots_list[-1][3] += sot.elib_publ_yrinc
				calc_maxpok(sots_list[-1][2])
				calc_maxpok(sots_list[-1][3])				
			elif _publ == 2:		
				sots_list[-1][2] += sot.otch_cit_rinc
				sots_list[-1][3] += sot.elib_cit_rinc
				calc_maxpok(sots_list[-1][2])
				calc_maxpok(sots_list[-1][3])				
			elif _publ == 3:		
				sots_list[-1][2] += sot.otch_hir_rinc
				sots_list[-1][3] += sot.elib_hir_rinc
				calc_maxpok(sots_list[-1][2])
				calc_maxpok(sots_list[-1][3])				

def set_fak(_publ, _year, _fak):
	global use_fak_sname, maxpok
	maxpok = 0
	kafs_list.clear()	
	use_fak_sname = Fakultet.objects.get(id=_fak).fakultet_sname
	if _year:
		for kaf in Kafedra.objects.filter(fakultet=_fak):
			kafs_list.append([kaf.id, kaf.kafedra_sname, kaf.kafedra_name, 0, 0, 0])
			kafs_list[-1][3] += len(Sotrud.objects.filter(kafedra=kaf.id))
			for sot in Sotrud.objects.filter(kafedra=kaf.id):			
				if _publ == 0:
					try:
						kafs_list[-1][4] += Year.objects.get(sotrud=sot.id, year = _year).otch_publ_rinc
						kafs_list[-1][5] += Year.objects.get(sotrud=sot.id, year = _year).elib_publ_rinc
						calc_maxpok(kafs_list[-1][4])
						calc_maxpok(kafs_list[-1][5])
					except Year.DoesNotExist:
						kafs_list[-1][4] += 0
						kafs_list[-1][5] += 0			
				elif _publ == 1:			
					try:
						kafs_list[-1][4] += Year.objects.get(sotrud=sot.id, year = _year).otch_publ_yrinc
						kafs_list[-1][5] += Year.objects.get(sotrud=sot.id, year = _year).elib_publ_yrinc
						calc_maxpok(kafs_list[-1][4])
						calc_maxpok(kafs_list[-1][5])						
					except Year.DoesNotExist:
						kafs_list[-1][4] += 0
						kafs_list[-1][5] += 0
				elif _publ == 2:	
					try:
						kafs_list[-1][4] += Year.objects.get(sotrud=sot.id, year = _year).otch_cit_rinc
						kafs_list[-1][5] += Year.objects.get(sotrud=sot.id, year = _year).elib_cit_rinc
						calc_maxpok(kafs_list[-1][4])
						calc_maxpok(kafs_list[-1][5])						
					except Year.DoesNotExist:
						kafs_list[-1][4] += 0
						kafs_list[-1][5] += 0
				elif _publ == 3:
					kafs_list[-1][4] += sot.otch_hir_rinc
					kafs_list[-1][5] += sot.elib_hir_rinc
					calc_maxpok(kafs_list[-1][4])
					calc_maxpok(kafs_list[-1][5])
	else:
		for kaf in Kafedra.objects.filter(fakultet=_fak):
			kafs_list.append([kaf.id, kaf.kafedra_sname, kaf.kafedra_name, 0, 0, 0])
			kafs_list[-1][3] += len(Sotrud.objects.filter(kafedra=kaf.id))
			for sot in Sotrud.objects.filter(kafedra=kaf.id):			
				if _publ == 0:
					kafs_list[-1][4] += sot.otch_publ_rinc
					kafs_list[-1][5] += sot.elib_publ_rinc
					calc_maxpok(kafs_list[-1][4])
					calc_maxpok(kafs_list[-1][5])
				elif _publ == 1:			
					kafs_list[-1][4] += sot.otch_publ_yrinc
					kafs_list[-1][5] += sot.elib_publ_yrinc
					calc_maxpok(kafs_list[-1][4])
					calc_maxpok(kafs_list[-1][5])					
				elif _publ == 2:		
					kafs_list[-1][4] += sot.otch_cit_rinc
					kafs_list[-1][5] += sot.elib_cit_rinc
					calc_maxpok(kafs_list[-1][4])
					calc_maxpok(kafs_list[-1][5])					
				elif _publ == 3:
					kafs_list[-1][4] += sot.otch_hir_rinc
					kafs_list[-1][5] += sot.elib_hir_rinc
					calc_maxpok(kafs_list[-1][4])
					calc_maxpok(kafs_list[-1][5])					

def set_fak_all(_publ, _year):
	global maxpok
	maxpok = 0
	faks_list.clear()
	faks = Fakultet.objects.all()
	if _year:
		for fak in faks:
			faks_list.append([fak.id, fak.fakultet_sname, fak.fakultet_name, 0, 0, 0, 0])
			faks_list[-1][3] = len(Kafedra.objects.filter(fakultet=fak.id))
			for kaf in Kafedra.objects.filter(fakultet=fak.id):				
				faks_list[-1][4] += len(Sotrud.objects.filter(kafedra=kaf.id))
				for sot in Sotrud.objects.filter(kafedra=kaf.id):
					if _publ == 0:
						try:
							faks_list[-1][5] += Year.objects.get(sotrud=sot.id, year = _year).otch_publ_rinc
							faks_list[-1][6] += Year.objects.get(sotrud=sot.id, year = _year).elib_publ_rinc
							calc_maxpok(faks_list[-1][5])
							calc_maxpok(faks_list[-1][6])
						except Year.DoesNotExist:
							faks_list[-1][5] += 0
							faks_list[-1][6] += 0													
					elif _publ == 1:
						try:
							faks_list[-1][5] += Year.objects.get(sotrud=sot.id, year = _year).otch_publ_yrinc
							faks_list[-1][6] += Year.objects.get(sotrud=sot.id, year = _year).elib_publ_yrinc
							calc_maxpok(faks_list[-1][5])
							calc_maxpok(faks_list[-1][6])							
						except Year.DoesNotExist:
							faks_list[-1][5] += 0
							faks_list[-1][6] += 0						
					elif _publ == 2:
						try:	
							faks_list[-1][5] += Year.objects.get(sotrud=sot.id, year = _year).otch_cit_rinc
							faks_list[-1][6] += Year.objects.get(sotrud=sot.id, year = _year).elib_cit_rinc
							calc_maxpok(faks_list[-1][5])
							calc_maxpok(faks_list[-1][6])							
						except Year.DoesNotExist:
							faks_list[-1][5] += 0
							faks_list[-1][6] += 0	
					elif _publ == 3:
						faks_list[-1][5] += sot.otch_hir_rinc
						faks_list[-1][6] += sot.elib_hir_rinc
						calc_maxpok(faks_list[-1][5])
						calc_maxpok(faks_list[-1][6])						
	else:	
		for fak in faks:
			faks_list.append([fak.id, fak.fakultet_sname, fak.fakultet_name, 0, 0, 0, 0])
			faks_list[-1][3] = len(Kafedra.objects.filter(fakultet=fak.id))
			for kaf in Kafedra.objects.filter(fakultet=fak.id):				
				faks_list[-1][4] += len(Sotrud.objects.filter(kafedra=kaf.id))
				for sot in Sotrud.objects.filter(kafedra=kaf.id):
					if _publ == 0:
						faks_list[-1][5] += sot.otch_publ_rinc
						faks_list[-1][6] += sot.elib_publ_rinc
						calc_maxpok(faks_list[-1][5])
						calc_maxpok(faks_list[-1][6])						
					elif _publ == 1:
						faks_list[-1][5] += sot.otch_publ_yrinc
						faks_list[-1][6] += sot.elib_publ_yrinc
						calc_maxpok(faks_list[-1][5])
						calc_maxpok(faks_list[-1][6])
					elif _publ == 2:
						faks_list[-1][5] += sot.otch_cit_rinc
						faks_list[-1][6] += sot.elib_cit_rinc
						calc_maxpok(faks_list[-1][5])
						calc_maxpok(faks_list[-1][6])						
					elif _publ == 3:
						faks_list[-1][5] += sot.otch_hir_rinc
						faks_list[-1][6] += sot.elib_hir_rinc				
						calc_maxpok(faks_list[-1][5])
						calc_maxpok(faks_list[-1][6])						

def index(request):
	publ = 0
	year = 0
	fak = 0
	kaf = 0

	if 'publ' in request.GET:

		if request.GET['publ'] == "1":
			publ = 1

		elif request.GET['publ'] == "2":
			publ = 2			

		elif request.GET['publ'] == "3":
			publ = 3

	if 'year' in request.GET and int(request.GET['year']):
		year = int(request.GET['year'])

	if 'kaf' in request.GET and int(request.GET['kaf']):
		kaf = request.GET['kaf']
		set_kaf(publ, year, request.GET['kaf'])
		return render(request, 'mainapp/index.html', {"date_obn" : DateObn.objects.get(id=1).date_time, 'sots_list' : sots_list, "use_fak_sname" : use_fak_sname, "use_kaf_sname" : use_kaf_sname, "publ" : publ, "year" : year, "fak" : fak, "kaf" : kaf, "maxpok" : maxpok})

	if 'fak' in request.GET and int(request.GET['fak']):
		fak = request.GET['fak']
		set_fak(publ, year, request.GET['fak'])
		return render(request, 'mainapp/index.html', {"date_obn" : DateObn.objects.get(id=1).date_time, 'kafs_list' : kafs_list, "use_fak_sname" : use_fak_sname, "publ" : publ, "year" : year, "fak" : fak, "kaf" : kaf, "maxpok" : maxpok})
	
	
	set_fak_all(publ, year)
	return render(request, 'mainapp/index.html', {"date_obn" : DateObn.objects.get(id=1).date_time, 'faks_list' : faks_list, "publ" : publ, "year" : year, "fak" : fak, "kaf" : kaf, "maxpok" : maxpok})
