import numpy as np
import math
from typing import Dict, List, Tuple


# Função principal de cálculo de pré-dimensionamento
def calcular_pre_dimensionamento():
    print("\n--- Cálculo de Pré-Dimensionamento ---")
    print("Opções de tipo de peça disponíveis: pilar, viga, laje, fundacao, arco, trelica, viga_continua, flecha, detalhamento")
    tipo_peca = input("Digite o tipo de peça desejado: ").strip().lower()

    if tipo_peca not in ["pilar", "viga", "laje", "fundacao", "arco", "trelica", "viga_continua", "flecha", "detalhamento"]:
        print("Tipo de peça não reconhecido. Escolha entre as opções disponíveis.")
        return

    try:
        largura = float(input("Digite a largura da peça em metros: "))
        altura = float(input("Digite a altura da peça em metros: "))
        carga = float(input("Digite a carga aplicada em kN: "))
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números para as dimensões e carga.")
        return

    if largura <= 0 or altura <= 0 or carga <= 0:
        print("A largura, altura e carga devem ser valores positivos.")
        return

    # Seleção do tipo de fundação
    if tipo_peca == "fundacao":
        escolher_tipo_fundacao(carga, largura, altura)
    else:
        calcular_elemento(tipo_peca, largura, altura, carga)

# Função para calcular elementos estruturais diferentes de fundação
def calcular_elemento(tipo_peca, largura, altura, carga):
    if tipo_peca == "pilar":
        pilar = Pilar(carga, largura, altura)
        print(pilar.gerar_relatorio())
    elif tipo_peca == "viga":
        comprimento = float(input("Digite o comprimento da viga em metros: "))
        viga = Viga(carga, largura, altura, comprimento)
        print(viga.gerar_relatorio())
    elif tipo_peca == "laje":
        laje = Laje(carga, largura, altura)
        print(laje.gerar_relatorio())
    elif tipo_peca == "arco":
        raio = float(input("Digite o raio do arco em metros: "))
        arco = Arco(carga, largura, altura, raio)
        print(arco.gerar_relatorio())
    elif tipo_peca == "trelica":
        trelica = Trelica(carga, largura, altura)
        print(trelica.gerar_relatorio())
    elif tipo_peca == "viga_continua":
        viga_continua = VigaContinua(carga, largura, altura)
        print(viga_continua.gerar_relatorio())
    elif tipo_peca == "flecha":
        flecha = Flecha(carga, largura, altura)
        print(flecha.gerar_relatorio())
    elif tipo_peca == "detalhamento":
        detalhamento = Detalhamento(carga, largura, altura)
        print(detalhamento.gerar_relatorio())

# Função de análise de estrutura 2D
def analisar_estrutura_2d(nos: List[Tuple[float, float]], barras: List[Tuple[int, int]], cargas: List[Tuple[int, float, float]], restricoes: List[Tuple[int, bool, bool]]) -> Dict:
    n_nos = len(nos)
    n_barras = len(barras)
    
    k_global = np.zeros((n_nos * 2, n_nos * 2))  # Matriz de rigidez global
    f_global = np.zeros(n_nos * 2)               # Vetor de forças globais
    
    # Propriedades do material e geométricas
    modulo_elasticidade = 210e9  # Pa para aço
    area_secao = 0.01            # m² (exemplo)

    # Montagem da matriz de rigidez global
    for barra in barras:
        n1, n2 = barra
        x1, y1 = nos[n1]
        x2, y2 = nos[n2]
        
        comprimento = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        cos_theta = (x2 - x1) / comprimento
        sin_theta = (y2 - y1) / comprimento
        
        # Matriz de rigidez da barra no sistema local
        k_local = (modulo_elasticidade * area_secao / comprimento) * np.array([
            [ cos_theta**2,  cos_theta*sin_theta, -cos_theta**2, -cos_theta*sin_theta],
            [ cos_theta*sin_theta,  sin_theta**2, -cos_theta*sin_theta, -sin_theta**2],
            [-cos_theta**2, -cos_theta*sin_theta,  cos_theta**2,  cos_theta*sin_theta],
            [-cos_theta*sin_theta, -sin_theta**2,  cos_theta*sin_theta,  sin_theta**2]
        ])
        
        # Mapear os índices globais dos nós
        indices = [n1 * 2, n1 * 2 + 1, n2 * 2, n2 * 2 + 1]
        
        # Adicionar a matriz de rigidez local à matriz global
        for i in range(4):
            for j in range(4):
                k_global[indices[i], indices[j]] += k_local[i, j]
    
    # Aplicação das cargas
    for carga in cargas:
        no, fx, fy = carga
        f_global[no * 2] += fx
        f_global[no * 2 + 1] += fy

    # Aplicação das restrições
    indices_livres = []
    for restricao in restricoes:
        no, restricao_x, restricao_y = restricao
        if not restricao_x:
            indices_livres.append(no * 2)
        if not restricao_y:
            indices_livres.append(no * 2 + 1)
    
    k_reduzida = k_global[np.ix_(indices_livres, indices_livres)]
    f_reduzida = f_global[indices_livres]

    # Cálculo dos deslocamentos
    deslocamentos = np.zeros(n_nos * 2)
    deslocamentos_livres = np.linalg.solve(k_reduzida, f_reduzida)
    for i, indice in enumerate(indices_livres):
        deslocamentos[indice] = deslocamentos_livres[i]

    # Cálculo das reações
    reacoes = np.dot(k_global, deslocamentos) - f_global
    
    # Preparação dos resultados
    resultados = {
        "Deslocamentos": [(deslocamentos[i * 2], deslocamentos[i * 2 + 1]) for i in range(n_nos)],
        "Reacoes": [(reacoes[i * 2], reacoes[i * 2 + 1]) for i in range(n_nos)]
    }

    return resultados
# Função de escolha do tipo de fundação
def escolher_tipo_fundacao(carga, largura, altura):
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
        sapata = SapataRigida(carga, largura, altura)
        print(sapata.gerar_relatorio())
    elif escolha == "2":
        sapata_associada = SapataAssociada(carga, largura, altura)
        print(sapata_associada.gerar_relatorio())
    elif escolha == "3":
        bloco_coroamento = BlocoDeCoroamento(carga, largura, altura)
        print(bloco_coroamento.gerar_relatorio())
    elif escolha == "4":
        tubulao = TubulaoCeuAberto(carga, largura, altura)
        print(tubulao.gerar_relatorio())
    elif escolha == "5":
        tubulao_ar = TubulaoSobArComprimido(carga, largura, altura)
        print(tubulao_ar.gerar_relatorio())
    elif escolha == "6":
        estaca_helice = EstacaHeliceContinua(carga, largura, altura)
        print(estaca_helice.gerar_relatorio())
    elif escolha == "7":
        radier = Radier(carga, largura, altura)
        print(radier.gerar_relatorio())
    elif escolha == "8":
        bloco_isolado = BlocoIsolado(carga, largura, altura)
        print(bloco_isolado.gerar_relatorio())
    else:
        print("Opção inválida. Escolha novamente.")

# Definições das classes para cada tipo de elemento estrutural e fundação

class Pilar:
    def __init__(self, carga, largura, altura):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        area_secao = self.largura * self.altura
        return {
            "Área do Pilar (m²)": area_secao,
            "Carga Aplicada (kN)": self.carga
        }

class Viga:
    def __init__(self, carga, largura, altura, comprimento):
        self.carga = carga
        self.largura = largura
        self.altura = altura
        self.comprimento = comprimento

    def gerar_relatorio(self) -> Dict[str, float]:
        momento_fletor = (self.carga * self.comprimento) / 8
        return {
            "Comprimento da Viga (m)": self.comprimento,
            "Momento Fletor (kN.m)": momento_fletor,
            "Carga Aplicada (kN)": self.carga
        }

class Laje:
    def __init__(self, carga, largura, altura):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        area = self.largura * self.altura
        return {
            "Área da Laje (m²)": area,
            "Carga Aplicada (kN)": self.carga
        }

class Arco:
    def __init__(self, carga, largura, altura, raio):
        self.carga = carga
        self.largura = largura
        self.altura = altura
        self.raio = raio

    def gerar_relatorio(self) -> Dict[str, float]:
        momento_fletor = (self.carga * self.raio) / 2
        return {
            "Raio do Arco (m)": self.raio,
            "Momento Fletor (kN.m)": momento_fletor,
            "Carga Aplicada (kN)": self.carga
        }

class Trelica:
    def __init__(self, carga, largura, altura):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        return {
            "Carga Aplicada (kN)": self.carga,
            "Largura da Treliça (m)": self.largura,
            "Altura da Treliça (m)": self.altura
        }

class VigaContinua:
    def __init__(self, carga, largura, altura):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        return {
            "Carga Aplicada (kN)": self.carga,
            "Largura da Viga Contínua (m)": self.largura,
            "Altura da Viga Contínua (m)": self.altura
        }

class Flecha:
    def __init__(self, carga, largura, altura):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        return {
            "Carga Aplicada (kN)": self.carga,
            "Largura da Flecha (m)": self.largura,
            "Altura da Flecha (m)": self.altura
        }

class Detalhamento:
    def __init__(self, carga, largura, altura):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        return {
            "Carga Aplicada (kN)": self.carga,
            "Largura do Detalhamento (m)": self.largura,
            "Altura do Detalhamento (m)": self.altura
        }

class SapataRigida:
    def __init__(self, carga, largura, altura):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        area_base = self.carga / 150  # Exemplo com tensão de solo de 150 kN/m²
        return {
            "Área Base da Sapata Rígida (m²)": area_base,
            "Carga Aplicada (kN)": self.carga
        }

class SapataAssociada:
    def __init__(self, carga, largura, altura):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        area = self.largura * 2  # Exemplo para sapata associada
        return {
            "Área da Sapata Associada (m²)": area,
            "Carga Aplicada (kN)": self.carga
        }

class BlocoDeCoroamento:
    def __init__(self, carga, largura, altura):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        area_base = self.largura * self.altura
        return {
            "Área do Bloco de Coroamento (m²)": area_base,
            "Carga Aplicada (kN)": self.carga
        }

class TubulaoCeuAberto:
    def __init__(self, carga, largura, altura):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        area_base = math.pi * (self.largura / 2) ** 2
        return {
            "Área do Tubulão a Céu Aberto (m²)": area_base,
            "Carga Aplicada (kN)": self.carga
        }

class TubulaoSobArComprimido:
    def __init__(self, carga, largura, altura):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        area_base = math.pi * (self.largura / 2) ** 2
        return {
            "Área do Tubulão com Ar Comprimido (m²)": area_base,
            "Carga Aplicada (kN)": self.carga
        }

class EstacaHeliceContinua:
    def __init__(self, carga, largura, altura):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        area_base = math.pi * (self.largura / 2) ** 2
        return {
            "Área da Estaca Hélice Contínua (m²)": area_base,
            "Carga Aplicada (kN)": self.carga
        }

class Radier:
    def __init__(self, carga, largura, altura):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        area_base = self.largura * self.altura
        return {
            "Área do Radier (m²)": area_base,
            "Carga Aplicada (kN)": self.carga
        }

class BlocoIsolado:
    def __init__(self, carga, largura, altura):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        area_base = self.largura * self.altura
        return {
            "Área do Bloco Isolado (m²)": area_base,
            "Carga Aplicada (kN)": self.carga
        }

# Função principal para a interface do usuário
def main():
    while True:
        print("\n--- Calculadora Estrutural Completa ---")
        print("Escolha uma opção:")
        print("1. Cálculo de pré-dimensionamento")
        print("2. Sair")
        opcao = input("Digite o número da opção desejada: ").strip()

        if opcao == "1":
            calcular_pre_dimensionamento()
        elif opcao == "2":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
