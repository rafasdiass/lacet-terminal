# app_calculator/calculator.py

import math

def calcular_pre_dimensionamento():
    print("\n--- Cálculo de Pré-Dimensionamento ---")
    tipo_peca = input("Digite o tipo de peça (pilar ou viga): ").lower()
    largura = float(input("Digite a largura da peça em metros: "))
    altura = float(input("Digite a altura da peça em metros: "))
    carga = float(input("Digite a carga aplicada em kN: "))

    if tipo_peca == "pilar":
        # Exemplo de cálculo básico de área de armadura para um pilar
        area_secao = largura * altura
        tensao_concreto = 25  # resistência característica do concreto (MPa)
        tensao_aco = 500  # resistência característica do aço (MPa)
        
        area_armadura = (carga * 1000) / (0.8 * tensao_aco + 0.2 * tensao_concreto * area_secao)
        print(f"Área necessária de armadura para o pilar: {area_armadura:.2f} cm²")

    elif tipo_peca == "viga":
        # Exemplo de cálculo para uma viga simples com momento fletor
        comprimento = float(input("Digite o comprimento da viga em metros: "))
        momento_fletor = (carga * comprimento) / 4
        d = altura * 0.85  # Altura útil da viga
        momento_resistente = 0.9 * largura * d * tensao_concreto / 1000  # kN.m

        if momento_fletor > momento_resistente:
            print("A viga precisa de reforço adicional.")
        else:
            print(f"A viga está dimensionada adequadamente. Momento resistente: {momento_resistente:.2f} kN.m")
    else:
        print("Tipo de peça não reconhecido. Escolha entre 'pilar' ou 'viga'.")
