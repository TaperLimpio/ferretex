from django import forms
from django.utils import timezone
from Pedido_app.models import Pedido

FILTRO_DECICIONES_1=(
    ('Todo','----'),
    ('activo','activo'),
    ('inactivo','inactivo'),
    ('tomado','tomado'),
    ('entregado','entregado')
)

class FiltroPedido(forms.Form):
    estado = forms.ChoiceField(choices=FILTRO_DECICIONES_1)
    filtra_por_fechar = forms.BooleanField(required=False)
    fecha_de_inicio = forms.DateTimeField(initial="1990-01-01 00:00:00")
    fecha_de_limite = forms.DateTimeField(initial=timezone.now())

class PedidoForm(forms.Form):
    n_tarjeta = forms.CharField(max_length=10)
    direccion = forms.CharField(max_length=40)
    