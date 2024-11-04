from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import datetime

def gerar_relatorio_pdf(dados_calculo):
    """
    Gera um relatório em PDF com os dados de cálculo fornecidos.

    :param dados_calculo: Dicionário contendo as informações dos cálculos realizados.
    """
    print("\n--- Geração de Relatório em PDF ---")
    nome_arquivo = f"relatorio_calculo_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    c = canvas.Canvas(nome_arquivo, pagesize=A4)
    c.setTitle("Relatório de Cálculo Estrutural - LCT Calculator")
    
    # Configurações de layout
    margem_esquerda = 50
    posicao_vertical = 800
    espacamento_linha = 20

    # Título do Relatório
    c.drawString(margem_esquerda, posicao_vertical, "Relatório de Cálculo Estrutural")
    posicao_vertical -= espacamento_linha
    c.drawString(margem_esquerda, posicao_vertical, "LCT Calculator")
    posicao_vertical -= espacamento_linha * 2

    # Informações de Data
    data_atual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    c.drawString(margem_esquerda, posicao_vertical, f"Data de geração do relatório: {data_atual}")
    posicao_vertical -= espacamento_linha * 2

    # Detalhes do Cálculo
    c.drawString(margem_esquerda, posicao_vertical, "Detalhes do Cálculo:")
    posicao_vertical -= espacamento_linha

    for chave, valor in dados_calculo.items():
        if isinstance(valor, dict):  # Para sub-itens de resultados, como armaduras
            c.drawString(margem_esquerda + 20, posicao_vertical, f"{chave}:")
            posicao_vertical -= espacamento_linha
            for sub_chave, sub_valor in valor.items():
                c.drawString(margem_esquerda + 40, posicao_vertical, f"{sub_chave}: {sub_valor}")
                posicao_vertical -= espacamento_linha
        else:
            c.drawString(margem_esquerda + 20, posicao_vertical, f"{chave}: {valor}")
            posicao_vertical -= espacamento_linha

        # Ajuste para evitar que o conteúdo ultrapasse a página
        if posicao_vertical < 100:
            c.showPage()
            posicao_vertical = 800
            c.drawString(margem_esquerda, posicao_vertical, "Continuação do Relatório de Cálculo Estrutural")
            posicao_vertical -= espacamento_linha * 2

    # Observações e Resultados
    posicao_vertical -= espacamento_linha
    c.drawString(margem_esquerda, posicao_vertical, "Conclusão do Cálculo:")
    posicao_vertical -= espacamento_linha
    conclusao = dados_calculo.get("Conclusão", "Os resultados estão dentro dos limites aceitáveis.")
    c.drawString(margem_esquerda + 20, posicao_vertical, conclusao)
    posicao_vertical -= espacamento_linha * 2

    # Assinatura e Finalização
    c.drawString(margem_esquerda, posicao_vertical, "-------------------------------")
    posicao_vertical -= espacamento_linha
    c.drawString(margem_esquerda, posicao_vertical, "Assinatura do engenheiro responsável")

    # Salva o arquivo PDF
    c.save()
    print(f"Relatório gerado com sucesso: {nome_arquivo}")

# Exemplo de uso:
# Passando um dicionário de exemplo para gerar o relatório
if __name__ == "__main__":
    dados_exemplo = {
        "Material": "Concreto",
        "Resistência característica": "25 MPa",
        "Carga aplicada": "500 kN",
        "Área da seção transversal": "300 cm²",
        "Tensão calculada": "16.67 MPa",
        "Armadura Longitudinal": {
            "Quantidade de Barras": 5,
            "Diâmetro das Barras (mm)": 20
        },
        "Armadura Transversal": {
            "Quantidade de Estribos": 3,
            "Diâmetro dos Estribos (mm)": 12
        },
        "Conclusão": "A tensão e armadura estão dentro dos limites aceitáveis para o concreto."
    }
    gerar_relatorio_pdf(dados_exemplo)
