from clientes.models import Cliente
from clientes.serializer import ClientesSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id', 'nome',]
    search_fields = ['nome', 'cpf',]
    filterset_fields = ['ativo',]
