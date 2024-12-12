from django import forms
from gestorProductos.models import Producto, Categoria
from django.core import validators

# Formulario básico
class ProductoForm(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.CharField()
    precio = forms.DecimalField()
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())
    stock = forms.IntegerField()

    nombre.widget.attrs['class'] = 'form-control'
    descripcion.widget.attrs['class'] = 'form-control'
    precio.widget.attrs['class'] = 'form-control'
    categoria.widget.attrs['class'] = 'form-control'
    stock.widget.attrs['class'] = 'form-control'

# Formulario basado en el modelo
class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(
        validators=[
            validators.MinLengthValidator(5),
            validators.MaxLengthValidator(100)
        ]
    )
    descripcion = forms.CharField()
    precio = forms.DecimalField()
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())
    stock = forms.IntegerField()

    class Meta:
        model = Producto
        exclude = ['creator']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['class'] = 'form-control'
