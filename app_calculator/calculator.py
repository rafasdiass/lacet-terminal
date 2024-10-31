# app_calculator/calculator.py

import numpy as np


def calcular_pre_dimensionamento():
    print("\n--- Cálculo de Pré-Dimensionamento ---")
    tipo_peca = input("Digite o tipo de peça ('pilar' ou 'viga'): ").strip().lower()

    # Validação do tipo de peça
    if tipo_peca not in ["pilar", "viga"]:
        print("Tipo de peça não reconhecido. Escolha entre 'pilar' ou 'viga'.")
        return

    try:
        largura = float(input("Digite a largura da peça em metros: "))
        altura = float(input("Digite a altura da peça em metros: "))
        carga = float(input("Digite a carga aplicada em kN: "))
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números para as dimensões e carga.")
        return

    # Verificação de valores positivos
    if largura <= 0 or altura <= 0 or carga <= 0:
        print("A largura, altura e carga devem ser valores positivos.")
        return

    if tipo_peca == "pilar":
        calcular_armadura_pilar(largura, altura, carga)
    elif tipo_peca == "viga":
        comprimento = float(input("Digite o comprimento da viga em metros: "))
        if comprimento <= 0:
            print("O comprimento deve ser um valor positivo.")
            return
        calcular_armadura_viga(largura, altura, carga, comprimento)


def calcular_armadura_pilar(largura, altura, carga):
    """
    Função para cálculo de área de armadura necessária para um pilar.
    """
    print("\n--- Cálculo de Armadura para Pilar ---")
    area_secao = largura * altura  # Área da seção transversal
    tensao_concreto = 25  # Resistência característica do concreto em MPa
    tensao_aco = 500  # Resistência característica do aço em MPa
    
    # Fórmula para área de armadura necessária em cm²
    area_armadura = (carga * 1000) / (0.8 * tensao_aco + 0.2 * tensao_concreto * area_secao)
    print(f"Área necessária de armadura para o pilar: {area_armadura:.2f} cm²")


def calcular_armadura_viga(largura, altura, carga, comprimento):
    """
    Função para cálculo de armadura e momento resistente para uma viga.
    """
    print("\n--- Cálculo de Armadura para Viga ---")
    tensao_concreto = 25  # Resistência característica do concreto em MPa
    momento_fletor = (carga * comprimento) / 4  # Momento fletor (exemplo de cálculo simplificado)
    d = altura * 0.85  # Altura útil da viga (fator de redução)

    # Momento resistente considerando a largura e altura da viga
    momento_resistente = 0.9 * largura * d * tensao_concreto / 1000  # Conversão para kN.m

    print(f"Momento fletor calculado: {momento_fletor:.2f} kN.m")
    print(f"Momento resistente da viga: {momento_resistente:.2f} kN.m")

    if momento_fletor > momento_resistente:
        print("A viga precisa de reforço adicional.")
    else:
        print("A viga está dimensionada adequadamente.")

    # Cálculo da área de armadura para a viga (exemplo simplificado)
    area_armadura_viga = momento_fletor / (tensao_concreto * d)
    print(f"Área necessária de armadura para a viga: {area_armadura_viga:.2f} cm²")


def analisar_estrutura_2d():
    """
    Função que realiza uma análise estrutural 2D de uma treliça usando operações de álgebra linear.
    Este exemplo cria um modelo básico de treliça entre três nós e calcula as reações.
    """
    print("\n--- Análise Estrutural 2D ---")

    # Definindo a matriz de rigidez global para três nós conectados
    # Exemplo de uma matriz de rigidez 2D simplificada para uma estrutura de treliça
    K = np.array([
        [1, 0, -1, 0, 0, 0],
        [0, 1, 0, -1, 0, 0],
        [-1, 0, 1, 0, 0, 0],
        [0, -1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, -1],
        [0, 0, 0, 0, -1, 1]
    ])

    # Vetor de forças aplicadas (aplicando uma carga de -10kN no nó 3 no eixo Y)
    F = np.array([0, 0, 0, 0, 0, -10])

    # Definindo restrições (suponha que o nó 1 está fixo em X e Y)
    # Eliminando as linhas e colunas correspondentes ao nó fixo para resolver o sistema
    K_reduzido = K[2:, 2:]
    F_reduzido = F[2:]

    # Resolvendo o sistema linear para os deslocamentos
    deslocamentos = np.linalg.solve(K_reduzido, F_reduzido)

    print("\n--- Resultados da Análise Estrutural ---")
    print("Deslocamentos nos graus de liberdade livres:")
    print(f"dx2 = {deslocamentos[0]:.5f} m, dy2 = {deslocamentos[1]:.5f} m")
    print(f"dx3 = {deslocamentos[2]:.5f} m, dy3 = {deslocamentos[3]:.5f} m")
