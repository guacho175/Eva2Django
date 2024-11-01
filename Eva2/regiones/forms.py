from django import forms
from .models import Detalle, Comuna, Region

class DetalleUpdateForm(forms.ModelForm):
    class Meta:
        model = Detalle
        fields = ['poblacion', 'codigo_postal', 'informacion', 'alcalde']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    

