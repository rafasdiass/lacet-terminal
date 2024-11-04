from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Estrutura, Fundacao, Carga
from .serializers import EstruturaSerializer, FundacaoSerializer, CargaSerializer

@api_view(['GET'])
def listar_estruturas(request):
    """
    Endpoint para listar todas as estruturas disponíveis.
    """
    estruturas = Estrutura.objects.all()
    serializer = EstruturaSerializer(estruturas, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def calcular_pre_dimensionamento(request):
    """
    Endpoint para enviar dados de cálculo e obter resultados.
    """
    serializer = CargaSerializer(data=request.data)
    if serializer.is_valid():
        carga = serializer.save()
        resultado = carga.calcular_pre_dimensionamento()
        return Response(resultado, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
