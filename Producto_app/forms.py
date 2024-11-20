from django import forms
from .models import Producto
from Sucursal_app.models import Sucursal

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','codigo', 'precio','stock','descripcion', 'imagen', 'sucursales','catalogo']

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.fields['sucursales'].queryset = Sucursal.objects.filter(estado='activo')

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock < 0:
            raise forms.ValidationError('Ingrese un cantidad de stock superior o igual a cero.')
        return stock

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if Producto.objects.filter(nombre=nombre).exists():
            raise forms.ValidationError('Este nombre ya está registrado. Elija un nombre diferente.')
        return nombre

    def clean_codigo(self):
        codigo = self.cleaned_data.get('codigo')
        if Producto.objects.filter(codigo=codigo).exists():
            raise forms.ValidationError('Este código ya está registrado. Elija un código diferente.')
        return codigo

