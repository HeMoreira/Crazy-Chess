import copy
from settings import settings
from models.enums_utilitarios import Jogador


def imprimirTabuleiro(): 
    tabuleiro_impressao = copy.deepcopy(settings.tabuleiro_principal)
    numeros_tabuleiro = settings.numeros_tabuleiro

    if settings.inversao_dinamica_esta_habilitada and settings.jogador_atual == Jogador.JOGADOR_DE_PRETAS:
        tabuleiro_impressao, numeros_tabuleiro = inverterOTabuleiroSeJogadorDePretas(tabuleiro_impressao)
    
    imprimirCampo(tabuleiro_impressao, numeros_tabuleiro)

def imprimirCampo(tabuleiro_impressao:list, numeros_tabuleiro:list[str]):
    impressao_final = ""
    print("   _______________________")
    linha_atual = 0 
    impressao_final = impressao_final + f"{numeros_tabuleiro[linha_atual]}" 
    linha_atual+=1 
    for linha, coluna in percorrerCadaCasaDoTabuleiro():
        impressao_final = impressao_final + " |" + tabuleiro_impressao[linha][coluna].aparencia
        if (coluna+1) % 8 == 0 and linha+1 != 8:
            impressao_final = impressao_final + " |\n" 
            impressao_final = impressao_final + f"{numeros_tabuleiro[linha_atual]}" 
            linha_atual+=1 
        elif (coluna+1) % 8 == 0:
            impressao_final = impressao_final + " |" 
    print(impressao_final) 
    print("   ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯") 
    print("    a  b  c  d  e  f  g  h")

def inverterOTabuleiroSeJogadorDePretas(tabuleiro_impressao:list):
    linha_contraria = 7
    numeros_tabuleiro_invertidos = settings.numeros_tabuleiro[::-1]
    for linha in range(len(tabuleiro_impressao)):
        tabuleiro_impressao[linha] = settings.tabuleiro_principal[linha_contraria]
        linha_contraria-=1
    return tabuleiro_impressao, numeros_tabuleiro_invertidos

def percorrerCadaCasaDoTabuleiro():
    for linha in range(8):
        for coluna in range(8):
            yield linha, coluna

def exibirMovimentosPossiveis(lista_de_cordenadas:list):
    for cordenada in lista_de_cordenadas:
        if settings.tabuleiro_principal[cordenada.indice_linha][cordenada.indice_coluna].classe == "vazio":
            settings.tabuleiro_principal[cordenada.indice_linha][cordenada.indice_coluna] = settings.movimento_possivel

def limparMovimentosPossiveis():
    for linha, coluna in percorrerCadaCasaDoTabuleiro():
        if settings.tabuleiro_principal[linha][coluna].aparencia == "•":
            settings.tabuleiro_principal[linha][coluna] = settings.espaco_vazio

def limparPassantsPossiveis():
    for linha, coluna in percorrerCadaCasaDoTabuleiro():
        if settings.tabuleiro_principal[linha][coluna].classe == "peao":
            settings.tabuleiro_principal[linha][coluna].passant_direita = False
            settings.tabuleiro_principal[linha][coluna].passant_esquerda = False