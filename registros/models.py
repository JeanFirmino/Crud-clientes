from django.db import models
from phone_field import PhoneField

# Create your models here.
class categorias(models.Model):
    nome = models.CharField(max_length=150, help_text='O seu nome completo')
    data_nascimento = models.CharField(max_length=10, help_text='Por favor use "-" para DD-MM-AAAA')
    # para a data do cadastro não aparecer na tela, necessita adicionar auto_now_add
    endereco = models.CharField(max_length=250,help_text='O seu endereço residêncial (País. Estado. Cidade. Endereço. Número. cep)')
    telefone = PhoneField(max_length=11, help_text='Telefone para contato ((XX) XXXXX-XXXX)')
    observacoes = models.TextField(null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural='categorias'
    def __str__(self):
        return self.nome
    #para eliminar o categoria object na tela e apresentar o nome do cadastrado

