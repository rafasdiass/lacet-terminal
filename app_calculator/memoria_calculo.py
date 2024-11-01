# app_calculator/memoria_calculo.py
import math
from typing import Dict

class MemoriaCalculo:
    def __init__(self, material: str, resistencia: float, carga: float, largura: float, altura: float):
        self.material = material.lower()
        self.resistencia = resistencia  # em MPa
        self.carga = carga  # em kN
        self.largura = largura  # em cm
        self.altura = altura  # em cm
        self.secao_transversal = self.calcular_secao_transversal()
        self.tensao_material = self.calcular_tensao()

    def calcular_secao_transversal(self) -> float:
        """Calcula a área da seção transversal em cm²."""
        return self.largura * self.altura

    def calcular_tensao(self) -> float:
        """Calcula a tensão aplicada no material."""
        # Converter carga para kN e área para cm² antes do cálculo
        return self.carga / self.secao_transversal

    def verificar_resistencia(self) -> str:
        """Verifica se a tensão está dentro da resistência permitida do material."""
        if self.tensao_material > self.resistencia:
            return "A tensão excede a resistência do material. Reforço necessário."
        else:
            return "Tensão dentro dos limites aceitáveis."

    def gerar_relatorio(self) -> str:
        """Gera a memória de cálculo detalhada."""
        memoria = f"--- Memória de Cálculo ---\n"
        memoria += f"Material: {self.material.capitalize()}\n"
        memoria += f"Resistência característica (fck/fyk): {self.resistencia} MPa\n"
        memoria += f"Carga aplicada: {self.carga} kN\n"
        memoria += f"Largura da seção: {self.largura} cm\n"
        memoria += f"Altura da seção: {self.altura} cm\n"
        memoria += f"Área da seção transversal: {self.secao_transversal:.2f} cm²\n"
        memoria += f"Tensão calculada: {self.tensao_material:.2f} MPa\n"
        memoria += self.verificar_resistencia()
        
        return memoria

    def salvar_relatorio(self, caminho: str = "memoria_calculo.txt"):
        """Salva o relatório da memória de cálculo em um arquivo de texto."""
        with open(caminho, 'w') as arquivo:
            arquivo.write(self.gerar_relatorio())
        print(f"Relatório salvo em: {caminho}")

def gerar_memoria_calculo():
    print("\n--- Geração de Memória de Cálculo ---")
    material = input("Digite o tipo de material (concreto/aco): ").strip().lower()
    resistencia = float(input("Digite a resistência característica do material em MPa: "))
    carga = float(input("Digite a carga aplicada em kN: "))
    largura = float(input("Digite a largura da seção em cm: "))
    altura = float(input("Digite a altura da seção em cm: "))

    memoria = MemoriaCalculo(material, resistencia, carga, largura, altura)
    
    # Exibe a memória de cálculo
    print(memoria.gerar_relatorio())
    
    # Pergunta ao usuário se deseja salvar o relatório
    salvar = input("Deseja salvar a memória de cálculo em um arquivo? (s/n): ").strip().lower()
    if salvar == 's':
        caminho = input("Digite o caminho do arquivo para salvar (ou pressione Enter para o padrão): ").strip()
        if not caminho:
            caminho = "memoria_calculo.txt"
        memoria.salvar_relatorio(caminho)
