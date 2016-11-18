from django import forms
from .models import Prestamo

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ('usuario', 'libro', 'fecha_prestamo', 'fecha_propuesta', 'fecha_devolucion',)