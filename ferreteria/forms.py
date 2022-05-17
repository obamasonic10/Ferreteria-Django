from django import forms
from .models import Producto
from .models import Solicitud


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = '__all__'


