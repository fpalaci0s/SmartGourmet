from django.urls import path
from gestorProductos.views import *

urlpatterns = [
    path('productos/', listarProductos, name='listar_productos'),
    path('addProducto/', registrarProductos, name='registrar_producto'),
    path('editProducto/<int:id>/', editarProductos, name='editar_producto'),
    path('deleteProducto/<int:id>/', eliminarProductos, name='eliminar_producto'),
    path('categorias/', listarCategorias, name='listar_categorias'),
    path('addCategoria/', registrarCategoria, name='registrar_categoria'),
    path('editCategoria/<int:id>/', editarCategoria, name='editar_categoria'),
    path('deleteCategoria/<int:id>/', eliminarCategoria, name='eliminar_categoria'),
]
