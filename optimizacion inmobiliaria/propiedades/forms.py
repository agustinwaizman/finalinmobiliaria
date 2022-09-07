from django.forms import ModelForm
from .models import Propiedad

class DepartamentoForm(ModelForm):
    class Meta:
        model = Propiedad
        fields = '__all__'