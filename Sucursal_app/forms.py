from django import forms
from Sucursal_app.models import Sucursal

class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields=["nombre","direccion","fono","imagen"]

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if Sucursal.objects.filter(nombre=nombre).exists():
            raise forms.ValidationError('Este nombre ya está registrado. Elija un nombre diferente.')
        return nombre
    
    def clean_direccion(self):
        direccion = self.cleaned_data.get('direccion')
        if Sucursal.objects.filter(direccion = direccion).exists():
            raise forms.ValidationError('Esta direccion ya está registrado. Elija una direccion diferente.')
        return direccion
    
class SucursalActualizarForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields=["nombre","direccion","fono","imagen"]

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        mismo = Sucursal.objects.get(id = self.instance.id)
        
        if mismo.nombre == nombre:
            return nombre
        elif Sucursal.objects.filter(nombre=nombre).exists():
            raise forms.ValidationError('Este nombre ya está registrado. Elija un nombre diferente.')
        return nombre
    
    def clean_direccion(self):
        direccion = self.cleaned_data.get('direccion')
        mismo = Sucursal.objects.get(id = self.instance.id)
        
        if mismo.direccion == direccion:
            return direccion
        elif Sucursal.objects.filter(direccion = direccion).exists():
            raise forms.ValidationError('Esta direccion ya está registrada. Elija una direccion diferente.')
        return direccion