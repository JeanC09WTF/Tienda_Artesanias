from django import forms
from .models import Reserva
#para las reservas
class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre', 'email', 'telefono', 'fecha', 'hora', 'comentarios']