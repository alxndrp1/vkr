from django.contrib import admin

from .models import Univer, Fakultet, Kafedra, Sotrud

admin.site.register(Univer)
admin.site.register(Fakultet)
admin.site.register(Kafedra)
admin.site.register(Sotrud)