from django import forms
from Pedido_app.models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ["direccion"]