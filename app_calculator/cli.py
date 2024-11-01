from app_calculator.pre_dimensionamento import calcular_pre_dimensionamento
from app_calculator.analise import analisar_estrutura_2d
from app_calculator.memoria_calculo import gerar_memoria_calculo
from app_calculator.relatorios import gerar_relatorio_pdf
from app_calculator.estruturas import Pilar, Viga, Laje, Arco, Trelica, VigaContinua, Flecha, Detalhamento

def solicitar_entrada(prompt):
    """
    Função auxiliar para solicitar entrada do usuário.
    Se o usuário digitar 'voltar', retorna None para indicar que ele deseja voltar ao menu principal.
    """
    entrada = input(prompt + " (ou digite 'voltar' para retornar ao menu principal): ").strip()
    if entrada.lower() == "voltar":
        return None
    return entrada

def run_cli():
    print("Bem-vindo ao LCT Calculator CLI!")

    while True:
        print("\nEscolha uma opção:")
        print("1. Cálculo de pré-dimensionamento de peça")
        print("2. Análise estrutural 2D (treliça)")
        print("3. Gerar memória de cálculo")
        print("4. Gerar relatório em PDF")
        print("5. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            calcular_pre_dimensionamento()
        elif escolha == "2":
            executar_analise_estrutura_2d()
        elif escolha == "3":
            gerar_memoria_calculo()
        elif escolha == "4":
            gerar_relatorio_pdf()
        elif escolha == "5":
            print("Saindo da CLI...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

def calcular_pre_dimensionamento():
    print("\n--- Cálculo de Pré-Dimensionamento ---")
    print("Opções de tipo de peça disponíveis: pilar, viga, laje, fundacao, arco, trelica, viga_continua, flecha, detalhamento")
    
    tipo_peca = solicitar_entrada("Digite o tipo de peça desejado")
    if tipo_peca is None:
        return  # Volta ao menu principal

    if tipo_peca not in ["pilar", "viga", "laje", "fundacao", "arco", "trelica", "viga_continua", "flecha", "detalhamento"]:
        print("Opção inválida. Tente novamente.")
        return

    try:
        largura = solicitar_entrada("Digite a largura da peça em metros")
        if largura is None:
            return
        largura = float(largura)

        altura = solicitar_entrada("Digite a altura da peça em metros")
        if altura is None:
            return
        altura = float(altura)

        carga = solicitar_entrada("Digite a carga aplicada em kN")
        if carga is None:
            return
        carga = float(carga)
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números para as dimensões e carga.")
        return

    if largura <= 0 or altura <= 0 or carga <= 0:
        print("A largura, altura e carga devem ser valores positivos.")
        return

    # Lógica para cálculo de pré-dimensionamento para tipos de peças específicos
    if tipo_peca == "pilar":
        pilar = Pilar(carga, largura, altura)
        relatorio = pilar.gerar_relatorio()
    elif tipo_peca == "viga":
        comprimento = solicitar_entrada("Digite o comprimento da viga em metros")
        if comprimento is None:
            return
        comprimento = float(comprimento)
        viga = Viga(carga, largura, altura, comprimento)
        relatorio = viga.gerar_relatorio()
    elif tipo_peca == "laje":
        laje = Laje(carga, largura, altura)
        relatorio = laje.gerar_relatorio()
    elif tipo_peca == "arco":
        raio = solicitar_entrada("Digite o raio do arco em metros")
        if raio is None:
            return
        raio = float(raio)
        arco = Arco(carga, largura, altura, raio)
        relatorio = arco.gerar_relatorio()
    elif tipo_peca == "trelica":
        trelica = Trelica(carga, largura, altura)
        relatorio = trelica.gerar_relatorio()
    elif tipo_peca == "viga_continua":
        viga_continua = VigaContinua(carga, largura, altura)
        relatorio = viga_continua.gerar_relatorio()
    elif tipo_peca == "flecha":
        flecha = Flecha(carga, largura, altura)
        relatorio = flecha.gerar_relatorio()
    elif tipo_peca == "detalhamento":
        detalhamento = Detalhamento(carga, largura, altura)
        relatorio = detalhamento.gerar_relatorio()
    else:
        print("Tipo de peça não implementado.")
        return

    # Exibe o relatório gerado para o tipo de peça selecionado
    print("\nRelatório de Pré-Dimensionamento:")
    for key, value in relatorio.items():
        print(f"{key}: {value}")

def executar_analise_estrutura_2d():
    print("\n--- Análise Estrutural 2D ---")
    
    # Coletando os dados dos nós
    nos = []
    n_nos = solicitar_entrada("Digite o número de nós na estrutura")
    if n_nos is None:
        return
    n_nos = int(n_nos)

    for i in range(n_nos):
        x = solicitar_entrada(f"Digite a coordenada X do nó {i + 1}")
        if x is None:
            return
        x = float(x)
        
        y = solicitar_entrada(f"Digite a coordenada Y do nó {i + 1}")
        if y is None:
            return
        y = float(y)
        
        nos.append((x, y))

    # Coletando os dados das barras
    barras = []
    n_barras = solicitar_entrada("Digite o número de barras na estrutura")
    if n_barras is None:
        return
    n_barras = int(n_barras)

    for i in range(n_barras):
        no1 = solicitar_entrada(f"Digite o índice do primeiro nó da barra {i + 1} (inicie com 0)")
        if no1 is None:
            return
        no1 = int(no1)
        
        no2 = solicitar_entrada(f"Digite o índice do segundo nó da barra {i + 1} (inicie com 0)")
        if no2 is None:
            return
        no2 = int(no2)
        
        barras.append((no1, no2))

    # Coletando as cargas aplicadas
    cargas = []
    n_cargas = solicitar_entrada("Digite o número de cargas aplicadas na estrutura")
    if n_cargas is None:
        return
    n_cargas = int(n_cargas)

    for i in range(n_cargas):
        no = solicitar_entrada(f"Digite o índice do nó onde a carga {i + 1} é aplicada (inicie com 0)")
        if no is None:
            return
        no = int(no)
        
        fx = solicitar_entrada(f"Digite a componente X da carga {i + 1} (kN)")
        if fx is None:
            return
        fx = float(fx)
        
        fy = solicitar_entrada(f"Digite a componente Y da carga {i + 1} (kN)")
        if fy is None:
            return
        fy = float(fy)
        
        cargas.append((no, fx, fy))

    # Coletando as restrições
    restricoes = []
    for i in range(n_nos):
        restricao_x = solicitar_entrada(f"O nó {i + 1} possui restrição em X? (s/n)").strip().lower()
        if restricao_x == 'voltar':
            return
        restricao_x = restricao_x == 's'

        restricao_y = solicitar_entrada(f"O nó {i + 1} possui restrição em Y? (s/n)").strip().lower()
        if restricao_y == 'voltar':
            return
        restricao_y = restricao_y == 's'
        
        restricoes.append((i, restricao_x, restricao_y))

    # Executando a análise estrutural 2D
    resultados = analisar_estrutura_2d(nos, barras, cargas, restricoes)
    
    # Exibindo os resultados
    print("\nResultados da Análise Estrutural 2D:")
    for i, (desloc, reacao) in enumerate(zip(resultados["Deslocamentos"], resultados["Reacoes"])):
        print(f"Nó {i+1}: Deslocamento = {desloc}, Reação = {reacao}")

if __name__ == "__main__":
    run_cli()
