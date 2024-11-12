from django import forms
from Pedido_app.models import Pedido

class PedidoForm(forms.Form):
    n_serie = forms.CharField(max_length=10)
    direccion = forms.CharField(max_length=40)
    