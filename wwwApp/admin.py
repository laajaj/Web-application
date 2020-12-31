from django.contrib import admin
from django.contrib.admin import AdminSite
from wwwApp.models import *

# Register your models here.


admin.site.register(Aeroport)
admin.site.register(Pilote)
admin.site.register(Vol)
admin.site.register(Avion)
admin.site.register(Client)
admin.site.register(Equipage)
admin.site.register(Billet)
admin.site.register(Liaison)



class MyAdminSite(AdminSite):
    AdminSite.site_header = 'Admistration de la compagnie aérienne'


admin_site = MyAdminSite(AdminSite)