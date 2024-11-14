from typing import Any
from django import forms 
from Usuario_app.models import Usuario
from itertools import cycle


def validar_rut(rut):
    rut = rut.upper().replace("-", "").replace(".", "")
    rut_aux = rut[:-1]
    dv = rut[-1:]

    if not rut_aux.isdigit() or not (1_000_000 <= int(rut_aux) <= 25_000_000):
        return False

    revertido = map(int, reversed(rut_aux))
    factors = cycle(range(2, 8))
    suma = sum(d * f for d, f in zip(revertido, factors))
    residuo = suma % 11

    if dv == 'K':
        return residuo == 1
    if dv == '0':
        return residuo == 11
    return residuo == 11 - int(dv)



FILTRO_DECICIONES_1=(
    ('Todo','----'),
    ('Administrador','administrador'),
    ('Usuario','usuario'),
    ('Repartidor','repartidor')
)

FILTRO_DECICIONES_2=(
    ('Todo','----'),
    ('Activo','activo'),
    ('Inactivo','inactivo')
)


class Filtro(forms.Form):
    tipo = forms.ChoiceField(choices=FILTRO_DECICIONES_1)
    estado = forms.ChoiceField(choices=FILTRO_DECICIONES_2)

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'fono', 'contraseña']
    
    def clean_fono(self):
        fono = self.cleaned_data.get('fono')
        if not fono.startswith('+') or not fono[1:].replace(' ', '').isdigit():
            raise forms.ValidationError('El número de teléfono debe ser numérico y puede incluir un código de país con +.')
        return fono

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError('El correo electrónico debe terminar en @gmail.com.')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado.')
        return email
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if Usuario.objects.filter(nombre=nombre).exists():
            raise forms.ValidationError('Utilice otro nombre.')
        return nombre


class UsuarioAdminForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['rut','nombre', 'email', 'fono', 'tipo','contraseña']

    """
    def clean_rut(self):
     rut = self.cleaned_data.get('rut')
     if Usuario.objects.filter(rut=rut).exists():
        raise forms.ValidationError('Este RUT ya está registrado.')
     return rut
    """

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if validar_rut(rut):
            raise forms.ValidationError('Este RUT no es valido')
        return rut
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError('El correo electrónico debe terminar en @gmail.com.')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado.')
        return email

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if Usuario.objects.filter(nombre=nombre).exists():
            raise forms.ValidationError('Utilice otro nombre.')
        return nombre    
    
    def clean_tipo(self):
        tipo = self.cleaned_data.get('tipo')
        if tipo not in ['administrador', 'repartidor']:
            raise forms.ValidationError('Tipo de usuario inválido.')
        return tipo

    def clean_fono(self):
        fono = self.cleaned_data.get('fono')
        if not fono.startswith('+') or not fono[1:].replace(' ', '').isdigit():
            raise forms.ValidationError('El número de teléfono debe ser numérico y puede incluir un código de país con +.')
        return fono
