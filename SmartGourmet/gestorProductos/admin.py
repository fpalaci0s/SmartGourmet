from django.contrib import admin
from gestorProductos.models import Producto, Categoria

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'precio', 'stock', 'categoria', 'creator']
    list_filter = ['categoria', 'creator']
    search_fields = ['nombre', 'descripcion']

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']

# Register your models here.
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)