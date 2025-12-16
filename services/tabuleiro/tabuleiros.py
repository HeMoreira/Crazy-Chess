import copy
from settings import settings

def imprimirTabuleiro(jogador): 
    impressao = ""
    tabuleiro_suporte = copy.deepcopy(settings.tabuleiro_principal)
    numeros_tabuleiro_suporte = settings.numeros_tabuleiro
    # Inversão dinâmica do tabuleiro conforme o jogador atual varia...
    """
    if jogador == False:
        ajudante = 7
        numeros_tabuleiro_suporte = ["","","","","","","",""] 
        for linha in range(len(tabuleiro_suporte)):
            tabuleiro_suporte[linha] = settings.tabuleiro_principal[ajudante]
            numeros_tabuleiro_suporte[linha] = numeros_tabuleiro[ajudante]
            ajudante-=1
    """
        
    print("   _______________________") 
    linha_atual = 0 
    impressao = impressao + f"{numeros_tabuleiro_suporte[linha_atual]}" 
    linha_atual+=1 
    for linha in range(len(tabuleiro_suporte)):
        for coluna in range(8):
            impressao = impressao + " |" + tabuleiro_suporte[linha][coluna].aparencia
            if (coluna+1) % 8 == 0 and linha+1 != 8:
                impressao = impressao + " |\n" 
                impressao = impressao + f"{numeros_tabuleiro_suporte[linha_atual]}" 
                linha_atual+=1 
            elif (coluna+1) % 8 == 0:
                impressao = impressao + " |" 
    print(impressao) 
    print("   ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯") 
    print("    a  b  c  d  e  f  g  h")

def novoTabuleiroVazio():
    tabuleiro = [[],[],[],[],[],[],[],[]]
    for i in range(8):
        tabuleiro[i] = [settings.espaco_vazio]*8
    return tabuleiro