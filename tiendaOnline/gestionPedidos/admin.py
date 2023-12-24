from django.contrib import admin

from gestionPedidos.models import *

# Register your models here.

#esta clase se crea para poder hacer modificaciones al panel de administrador
class ClienteAdmin(admin.ModelAdmin):# ver que campos podemos observar en el administrador de la clase clientes
    list_display = ('nombre','direccion','telefono')#para que aparezca los campos que deseamos observar en el panel del admin
    search_fields = ('nombre','telefono')#es para poder buscar 


#esto es para poder filtrar
class ArticuloAdmin(admin.ModelAdmin):
    list_filter = ('seccion',)

class PedidosAdmin(admin.ModelAdmin):
    list_display = ('numero','fecha',)
    list_filter = ('fecha',)
    date_hierarchy = 'fecha'

admin.site.register(Cliente, ClienteAdmin)#tenemos que poner nuestra nueva clase 
admin.site.register(Articulos,ArticuloAdmin)#
admin.site.register(Pedidos,PedidosAdmin)