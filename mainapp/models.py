from django.db import models

class Univer(models.Model):
	univer_name = models.CharField('Наименование университета', max_length = 200)
	orgsid_univer = models.BigIntegerField('OrgsID на elibrary.ru ')

class Fakultet(models.Model):
	univer = models.ForeignKey(Univer, on_delete = models.CASCADE)
	fakultet_name = models.CharField('Наименование факультета', max_length = 200)

class Kafedra(models.Model):
	fakultet = models.ForeignKey(Fakultet, on_delete = models.CASCADE)
	kafedra_name = models.CharField('Наименование кафедры', max_length = 200)

class Sotrud(models.Model):
	kafedra = models.ForeignKey(Kafedra, on_delete = models.CASCADE)
	fio_sotrud = models.TextField('ФИО сотрудника')
	authorid_sotrud = models.BigIntegerField('AuthorID на elibrary.ru')

