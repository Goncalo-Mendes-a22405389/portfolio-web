from django import forms    # formulários Django
from .models import *   

class ProjetoForm(forms.ModelForm):
  class Meta:
    model = Projeto      
    fields = '__all__'  

class TecnologiaForm(forms.ModelForm):
  class Meta:
    model = Tecnologia
    fields = '__all__'