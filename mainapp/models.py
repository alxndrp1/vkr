from django.db import models

class Univer(models.Model):
	univer_name = models.CharField('нименование университета', max_length = 200)
	kol_vo_sotrud = models.IntegerField('кол-во сотрудников')
	kol_vo_kafedr = models.IntegerField('кол-во кафедр')

class Sotrud(models.Model):
	univer = models.ForeignKey(Univer, on_delete = models.CASCADE)
	fio_sotrud = models.TextField('ФИО сотрудника')

