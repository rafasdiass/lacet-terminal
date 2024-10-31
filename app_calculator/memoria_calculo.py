# app_calculator/memoria_calculo.py

def gerar_memoria_calculo():
    print("\n--- Geração de Memória de Cálculo ---")
    material = input("Digite o tipo de material (concreto/aco): ").lower()
    resistencia = float(input("Digite a resistência característica do material em MPa: "))
    carga = float(input("Digite a carga aplicada em kN: "))
    secao = float(input("Digite a área da seção transversal em cm²: "))
    
    # Cálculo fictício de área de armadura e verificação de tensão
    tensao_material = carga / secao  # Tensão = Força / Área
    memoria = f"Material: {material.capitalize()}, Resistência: {resistencia} MPa, Carga: {carga} kN, Tensão calculada: {tensao_material:.2f} MPa"
    
    if tensao_material > resistencia:
        memoria += "\nA tensão excede a resistência do material. Reforço necessário."
    else:
        memoria += "\nTensão dentro dos limites aceitáveis."

    print(memoria)
