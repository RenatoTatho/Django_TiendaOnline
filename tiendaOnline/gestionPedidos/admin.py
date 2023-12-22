from django.contrib import admin

from gestionPedidos.models import *

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):# ver que campos podemos observar en el administrador de la clase clientes
    list_display = ('nombre','direccion','telefono')#para que aparezca los campos que deseamos observar en el panel del admin
    search_fields = ('nombre','telefono')#es para poder buscar 


admin.site.register(Cliente, ClienteAdmin)#tenemos que poner nuestra nueva clase 
admin.site.register(Articulos)
admin.site.register(Pedidos)