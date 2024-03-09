from django.contrib import admin

# Register your models here.
from .models import Exicuters, Reestr_oferts, Filials, Location, Contract_Data



admin.site.register(Exicuters)
admin.site.register(Reestr_oferts)
admin.site.register(Filials)
admin.site.register(Location)
admin.site.register(Contract_Data)