# app_calculator/analise.py

import numpy as np
import math
from typing import Dict, List, Tuple

def analisar_estrutura_2d(
    nos: List[Tuple[float, float]],
    barras: List[Tuple[int, int]],
    cargas: List[Tuple[int, float, float]],
    restricoes: List[Tuple[int, bool, bool]]
) -> Dict:
    """
    Função para análise de uma estrutura 2D composta de barras.
    
    :param nos: Lista de coordenadas dos nós [(x, y), ...].
    :param barras: Lista de pares de índices dos nós que definem cada barra [(nó1, nó2), ...].
    :param cargas: Lista de cargas aplicadas [(nó, força_x, força_y), ...].
    :param restricoes: Lista de restrições aplicadas [(nó, restricao_x, restricao_y), ...].
    :return: Dicionário contendo os deslocamentos e as reações em cada nó.
    """
    # Inicialização do número de nós e barras
    n_nos = len(nos)
    k_global = np.zeros((n_nos * 2, n_nos * 2))  # Matriz de rigidez global
    f_global = np.zeros(n_nos * 2)               # Vetor de forças globais

    # Definindo propriedades do material e geométricas (pode ser ajustado para diferentes materiais)
    modulo_elasticidade = 210e9  # Módulo de elasticidade para aço em Pa
    area_secao = 0.01            # Área da seção transversal em metros quadrados

    # Montagem da matriz de rigidez global da estrutura
    for barra in barras:
        n1, n2 = barra
        x1, y1 = nos[n1]
        x2, y2 = nos[n2]
        
        comprimento = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        cos_theta = (x2 - x1) / comprimento
        sin_theta = (y2 - y1) / comprimento
        
        # Matriz de rigidez local para cada barra no sistema local de coordenadas
        k_local = (modulo_elasticidade * area_secao / comprimento) * np.array([
            [ cos_theta**2,  cos_theta*sin_theta, -cos_theta**2, -cos_theta*sin_theta],
            [ cos_theta*sin_theta,  sin_theta**2, -cos_theta*sin_theta, -sin_theta**2],
            [-cos_theta**2, -cos_theta*sin_theta,  cos_theta**2,  cos_theta*sin_theta],
            [-cos_theta*sin_theta, -sin_theta**2,  cos_theta*sin_theta,  sin_theta**2]
        ])
        
        # Mapeamento dos índices globais dos nós para posicionamento na matriz de rigidez global
        indices = [n1 * 2, n1 * 2 + 1, n2 * 2, n2 * 2 + 1]
        
        # Adicionando a matriz de rigidez local à matriz global da estrutura
        for i in range(4):
            for j in range(4):
                k_global[indices[i], indices[j]] += k_local[i, j]

    # Aplicação das cargas nodais no vetor de forças globais
    for carga in cargas:
        no, fx, fy = carga
        f_global[no * 2] += fx
        f_global[no * 2 + 1] += fy

    # Determinação dos índices livres, considerando as restrições impostas nos nós
    indices_livres = []
    for restricao in restricoes:
        no, restricao_x, restricao_y = restricao
        if not restricao_x:
            indices_livres.append(no * 2)
        if not restricao_y:
            indices_livres.append(no * 2 + 1)
    
    # Extraindo a submatriz de rigidez reduzida e o vetor de forças reduzido
    k_reduzida = k_global[np.ix_(indices_livres, indices_livres)]
    f_reduzida = f_global[indices_livres]

    # Cálculo dos deslocamentos apenas nos graus de liberdade livres
    deslocamentos = np.zeros(n_nos * 2)
    deslocamentos_livres = np.linalg.solve(k_reduzida, f_reduzida)
    for i, indice in enumerate(indices_livres):
        deslocamentos[indice] = deslocamentos_livres[i]

    # Cálculo das reações utilizando os deslocamentos calculados
    reacoes = np.dot(k_global, deslocamentos) - f_global

    # Preparação dos resultados em um dicionário
    resultados = {
        "Deslocamentos": [(deslocamentos[i * 2], deslocamentos[i * 2 + 1]) for i in range(n_nos)],
        "Reacoes": [(reacoes[i * 2], reacoes[i * 2 + 1]) for i in range(n_nos)]
    }

    return resultados
