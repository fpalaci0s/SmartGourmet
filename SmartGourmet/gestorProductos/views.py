from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from gestorProductos.models import Producto, Categoria
from gestorProductos.forms import ProductoForm, CategoriaForm

def is_admin(user):
    return user.is_superuser

@login_required
def listarProductos(request):
    if request.user.is_superuser:
        productos = Producto.objects.all()
    else:
        productos = Producto.objects.filter(creator=request.user)
    return render(request, 'gestorProductos/productos.html', {'productos': productos})

@login_required
def registrarProductos(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.creator = request.user
            producto.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'gestorProductos/addProducto.html', {'form': form})

@login_required
def editarProductos(request, id):
    producto = get_object_or_404(Producto, id=id)
    if not request.user.is_superuser and producto.creator != request.user:
        return HttpResponseForbidden("No tienes permiso para editar este producto")
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'gestorProductos/editProducto.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def eliminarProductos(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'gestorProductos/deleteProducto.html', {'producto': producto})

# Vistas para Categorías (solo admin)
@login_required
@user_passes_test(is_admin)
def listarCategorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'gestorProductos/categorias.html', {'categorias': categorias})

@login_required
@user_passes_test(is_admin)
def registrarCategoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'gestorProductos/addCategoria.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def editarCategoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'gestorProductos/editCategoria.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def eliminarCategoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('listar_categorias')
    return render(request, 'gestorProductos/deleteCategoria.html', {'categoria': categoria})