from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validade(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"O número de CPF é inválido"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"Não inclua números nesse campo"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"O RG deve ter 9 digitos"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O numero de celular deve seguir este modelo: 11 91234-1234. (respeitando espaços e traços)"})
        return data
    