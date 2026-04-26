from django import forms    # formulários Django
from .models import *   

class ProjetoForm(forms.ModelForm):
  class Meta:
    model = Projeto      
    fields = '__all__'  