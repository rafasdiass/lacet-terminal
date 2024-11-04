from typing import Dict
from estruturas import (
    SapataRigida,
    SapataAssociada,
    BlocoDeCoroamento,
    TubulaoCeuAberto,
    TubulaoSobArComprimido,
    EstacaHeliceContinua,
    Radier,
    BlocoIsolado
)

def escolher_tipo_fundacao(carga: float, largura: float, altura: float) -> Dict[str, float]:
    """
    Função que exibe as opções de tipo de fundação ao usuário e instancia
    a classe correspondente para calcular os parâmetros de fundação com base na carga,
    largura e altura fornecidos.

    Parâmetros:
    - carga (float): A carga aplicada na fundação em kN.
    - largura (float): A largura da fundação em metros.
    - altura (float): A altura da fundação em metros.

    Retorno:
    - Dict[str, float]: Um dicionário com os resultados do cálculo da fundação.
    """
    print("\n--- Tipos de Fundação ---")
    print("1. Sapata Rígida")
    print("2. Sapata Associada")
    print("3. Bloco de Coroamento")
    print("4. Tubulão Céu Aberto")
    print("5. Tubulão com Ar Comprimido")
    print("6. Estaca Hélice Contínua")
    print("7. Radier")
    print("8. Bloco Isolado")

    escolha = input("Escolha o tipo de fundação: ")
    
    if escolha == "1":
        return SapataRigida(carga, largura, altura).gerar_relatorio()
    elif escolha == "2":
        return SapataAssociada(carga, largura, altura).gerar_relatorio()
    elif escolha == "3":
        return BlocoDeCoroamento(carga, largura, altura).gerar_relatorio()
    elif escolha == "4":
        return TubulaoCeuAberto(carga, largura, altura).gerar_relatorio()
    elif escolha == "5":
        return TubulaoSobArComprimido(carga, largura, altura).gerar_relatorio()
    elif escolha == "6":
        return EstacaHeliceContinua(carga, largura, altura).gerar_relatorio()
    elif escolha == "7":
        return Radier(carga, largura, altura).gerar_relatorio()
    elif escolha == "8":
        return BlocoIsolado(carga, largura, altura).gerar_relatorio()
    else:
        print("Opção inválida. Escolha novamente.")
        return {}
