from django.forms import ModelForm
from .models import categorias
class categoriasform(ModelForm):
    class Meta:
        model = categorias
        fields = ['nome','data_nascimento','endereco','telefone','observacoes']