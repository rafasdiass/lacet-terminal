# app_calculator/cli.py

from app_calculator.calculator import calcular_pre_dimensionamento, analisar_estrutura_2d
from app_calculator.memoria_calculo import gerar_memoria_calculo
from app_calculator.relatorios import gerar_relatorio_pdf

def run_cli():
    """
    Função principal da CLI para o LCT Calculator.
    Permite ao usuário selecionar uma operação de cálculo estrutural ou de geração de relatórios.
    """
    print("Bem-vindo ao LCT Calculator CLI!")
    
    while True:
        print("\nEscolha uma opção:")
        print("1. Calcular pré-dimensionamento de peça")
        print("2. Análise estrutural 2D (treliça)")
        print("3. Gerar memória de cálculo")
        print("4. Gerar relatório em PDF")
        print("5. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            calcular_pre_dimensionamento()
        elif escolha == "2":
            analisar_estrutura_2d()
        elif escolha == "3":
            gerar_memoria_calculo()
        elif escolha == "4":
            gerar_relatorio_pdf()
        elif escolha == "5":
            print("Saindo da CLI...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Executa a CLI apenas se o script for executado diretamente
if __name__ == "__main__":
    run_cli()
