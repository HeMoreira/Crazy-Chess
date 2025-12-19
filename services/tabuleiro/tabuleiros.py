import copy
from settings import settings
from models.enums_utilitarios import Jogador

def imprimirTabuleiro(): 
    tabuleiro_impressao = copy.deepcopy(settings.tabuleiro_principal)
    numeros_tabuleiro = settings.numeros_tabuleiro

    if settings.inversao_dinamica_esta_habilitada and settings.jogador_atual == Jogador.JOGADOR_DE_PRETAS.value:
        tabuleiro_impressao, numeros_tabuleiro = inverterOTabuleiroSeJogadorDePretas(tabuleiro_impressao)
    
    imprimirCampo(tabuleiro_impressao, numeros_tabuleiro)

def imprimirCampo(tabuleiro_impressao:list, numeros_tabuleiro:list[str]):
    impressao_final = ""
    print("   _______________________")
    linha_atual = 0 
    impressao_final = impressao_final + f"{numeros_tabuleiro[linha_atual]}" 
    linha_atual+=1 
    for linha in range(len(tabuleiro_impressao)):
        for coluna in range(8):
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


def criarNovoTabuleiroVazio():
    tabuleiro = [[],[],[],[],[],[],[],[]]
    for i in range(8):
        tabuleiro[i] = [settings.espaco_vazio]*8
    return tabuleiro

def inverterOTabuleiroSeJogadorDePretas(tabuleiro_impressao:list):
    linha_contraria = 7
    numeros_tabuleiro_invertidos = settings.numeros_tabuleiro[::-1]
    for linha in range(len(tabuleiro_impressao)):
        tabuleiro_impressao[linha] = settings.tabuleiro_principal[linha_contraria]
        linha_contraria-=1
    return tabuleiro_impressao, numeros_tabuleiro_invertidos