from django.contrib import admin
from clientes.models import Cliente

class Clientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cpf', 'rg', 'celular', 'ativo')
    list_display_links = ('id', 'nome', 'cpf' )
    search_fields = ('id', 'nome', 'cpf' )
    list_per_page = 20
    ordering = ['id','nome']

admin.site.register(Cliente, Clientes)
