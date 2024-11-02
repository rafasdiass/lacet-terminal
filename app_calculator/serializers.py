from rest_framework import serializers
from .models import Estrutura, Fundacao, Carga

class EstruturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estrutura
        fields = '__all__'

class FundacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fundacao
        fields = '__all__'

class CargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carga
        fields = ['tipo_peca', 'largura', 'altura', 'carga', 'comprimento', 'raio']

    def create(self, validated_data):
        """
        Lógica para salvar a carga e calcular o pré-dimensionamento.
        """
        carga = Carga.objects.create(**validated_data)
        return carga
