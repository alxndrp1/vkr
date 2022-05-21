from django.contrib import admin

from .models import Fakultet, Kafedra, Sotrud, Year, DateObn

admin.site.register(Fakultet)
admin.site.register(Kafedra)
admin.site.register(Sotrud)
admin.site.register(Year)
admin.site.register(DateObn)
