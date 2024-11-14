from django import forms
from .models import Catalogo

class CatalogoForm(forms.ModelForm):
    class Meta:
        model = Catalogo
        fields = ['nombre', 'descripcion', 'imagen']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if Catalogo.objects.filter(nombre=nombre).exists():
            raise forms.ValidationError('Este nombre ya está registrado. Elija un nombre diferente.')
        return nombre

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if Catalogo.objects.filter(descripcion=descripcion).exists():
            raise forms.ValidationError('Esta descripción ya está registrada. Elija una descripción diferente.')
        return descripcion


class CantidadProducto(forms.Form):
    cantidad = forms.IntegerField()

    def cantidad_minima(self):
        can = self.cleaned_data.get('cantidad')
        if can < 0:
            raise forms.ValidationError('Porfavor ingrese la cantidad que desea.')
        return can