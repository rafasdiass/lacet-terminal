# app_calculator/cli.py

from app_calculator.calculator import calcular_pre_dimensionamento
from app_calculator.memoria_calculo import gerar_memoria_calculo
from app_calculator.relatorios import gerar_relatorio_pdf

def run_cli():
    print("Bem-vindo ao LCT Calculator CLI!")
    
    while True:
        print("\nEscolha uma opção:")
        print("1. Calcular pré-dimensionamento de peça")
        print("2. Gerar memória de cálculo")
        print("3. Gerar relatório em PDF")
        print("4. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            calcular_pre_dimensionamento()
        elif escolha == "2":
            gerar_memoria_calculo()
        elif escolha == "3":
            gerar_relatorio_pdf()
        elif escolha == "4":
            print("Saindo da CLI...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")
