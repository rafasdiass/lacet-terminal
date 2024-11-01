import math

def calcular_area_retangular(largura: float, altura: float) -> float:
    """Calcula a área de um retângulo."""
    return largura * altura

def calcular_area_circular(diametro: float) -> float:
    """Calcula a área de um círculo dado o diâmetro."""
    raio = diametro / 2
    return math.pi * raio ** 2

def calcular_volume_cilindrico(diametro: float, altura: float) -> float:
    """Calcula o volume de um cilindro com base no diâmetro e altura."""
    area_base = calcular_area_circular(diametro)
    return area_base * altura

def calcular_momento_fletor(carga: float, comprimento: float) -> float:
    """Calcula o momento fletor máximo para uma carga distribuída em uma viga simplesmente apoiada."""
    return (carga * comprimento) / 8

def calcular_forca_cisalhante(carga: float, comprimento: float) -> float:
    """Calcula a força de cisalhamento máxima para uma carga distribuída em uma viga."""
    return carga / 2

def calcular_tensao_normal(carga: float, area: float) -> float:
    """Calcula a tensão normal dada a carga e a área de aplicação."""
    return carga / area if area > 0 else 0

def calcular_peso_concreto(volume: float, peso_especifico: float = 25) -> float:
    """Calcula o peso do concreto, assumindo um peso específico padrão de 25 kN/m³."""
    return volume * peso_especifico

def verificar_resistencia_material(tensao_aplicada: float, resistencia_material: float) -> str:
    """Verifica se a tensão aplicada está dentro dos limites de resistência do material."""
    if tensao_aplicada > resistencia_material:
        return "A tensão excede a resistência do material. Reforço necessário."
    else:
        return "Tensão dentro dos limites aceitáveis."
