from django.db import models

#class Univer(models.Model):
#	univer_name = models.CharField('Наименование университета', max_length = 200)
#	orgsid_univer = models.BigIntegerField('OrgsID на elibrary.ru ')

class Fakultet(models.Model):
	fakultet_sname = models.CharField('Сокращенное наименование факультета', max_length = 100)
	fakultet_name = models.CharField('Наименование факультета', max_length = 200)

class Kafedra(models.Model):
	fakultet = models.ForeignKey(Fakultet, on_delete = models.CASCADE)
	kafedra_sname = models.CharField('Сокращенное наименование кафедры', max_length = 200)
	kafedra_name = models.CharField('Наименование кафедры', max_length = 200)

class Sotrud(models.Model):
	kafedra = models.ForeignKey(Kafedra, on_delete = models.CASCADE)
	fio_s = models.CharField('Фамилия И О', max_length = 200)
	fio = models.TextField('Фамилия Имя Отчество')
	authorid_sotrud = models.BigIntegerField('AuthorID на elibrary.ru')
	
	elib_publ_rinc = models.IntegerField('Публикаций в РИНЦ (elibrary)')
	elib_publ_yrinc = models.IntegerField('Публикации входящие в ядро РИНЦ (elibrary)')
	elib_cit_rinc = models.IntegerField('Цитирования публикаций в РИНЦ (elibrary)')
	elib_hir_rinc = models.IntegerField('Индекс Хирша по публикациям в РИНЦ (elibrary)')

	otch_publ_rinc = models.IntegerField('Публикаций в РИНЦ (отчетные)')
	otch_publ_yrinc = models.IntegerField('Публикации входящие в ядро РИНЦ (отчетные)')
	otch_cit_rinc = models.IntegerField('Цитирования публикаций в РИНЦ (отчетные)')
	otch_hir_rinc = models.IntegerField('Индекс Хирша по публикациям в РИНЦ (отчетные)')

class Year(models.Model):
	sotrud = models.ForeignKey(Sotrud, on_delete = models.CASCADE)
	year = models.CharField('Год', max_length = 100)
	elib_publ_rinc = models.IntegerField('Публикаций в РИНЦ (elibrary)')
	elib_publ_yrinc = models.IntegerField('Публикации входящие в ядро РИНЦ (elibrary)')
	elib_cit_rinc = models.IntegerField('Цитирования публикаций в РИНЦ (elibrary)')

	otch_publ_rinc = models.IntegerField('Публикаций в РИНЦ (отчетные)')
	otch_publ_yrinc = models.IntegerField('Публикации входящие в ядро РИНЦ (отчетные)')
	otch_cit_rinc = models.IntegerField('Цитирования публикаций в РИНЦ (отчетные)')

class DateObn(models.Model):
	date_time = models.CharField('Дата и время', max_length = 200)