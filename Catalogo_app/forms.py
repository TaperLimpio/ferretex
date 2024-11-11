from django import forms
from .models import Catalogo

class CatalogoForm(forms.ModelForm):
    class Meta:
        model = Catalogo
        fields = ['nombre', 'descripcion', 'imagen']

class CantidadProducto(forms.Form):
    cantidad = forms.IntegerField()

    def cantidad_minima(self):
        can = self.cleaned_data.get('cantidad')
        if can < 0:
            raise forms.ValidationError('Porfavor ingrese la cantidad que desea.')
        return can