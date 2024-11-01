""" fornms.py
 """
from django import forms
from .models import Detalle
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DetalleUpdateForm(forms.ModelForm):
    class Meta:
        model = Detalle
        fields = ['poblacion', 'codigo_postal', 'informacion', 'alcalde']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

        # Cambiar el widget de 'codigo_postal' a un campo de texto
        self.fields['codigo_postal'].widget = forms.TextInput(attrs={'class': 'form-control'})



# regiones/forms.py



class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo Electrónico")
    first_name = forms.CharField(required=True, label="Nombre")
    last_name = forms.CharField(required=True, label="Apellido")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']




class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=True,
        label='Nombre de usuario',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        required=True,
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
