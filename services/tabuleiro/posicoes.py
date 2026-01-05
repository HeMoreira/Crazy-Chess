from settings import settings
from services.tabuleiro import pecas
from models.cords import Cordenadas
from models.enums_utilitarios import Jogador

def ObterCordenadaValida(posicoes:str):
    cordenada_y = validarCordenadaY(posicoes[0])
    cordenada_x = validarCordenadaX(posicoes[1])
    cordenadas_da_posicao = Cordenadas(cordenada_x, cordenada_y)
    return cordenadas_da_posicao

def validarCordenadaY(posicao_y:str):
    for chave, valor in settings.conversao_coluna.items():
        if chave == posicao_y:
            return valor-1
    return -1

def validarCordenadaX(posicao_x:str):
    if posicao_x in settings.numeros_tabuleiro:
        return 8-(int(posicao_x))
    return -1

def testarValidezCoordenadas(cordenadas:Cordenadas, tabuleiro:list):
    if testarSeCordenadasSaoValidas(cordenadas) == False:
        print("! Coordenada Inválida, as coordenadas só podem ter 2 ou 4 caractéres..")
        return False
    else:
        if testarSeExistePecaNasCordenadas(cordenadas, tabuleiro) == False:
            print("! Coordenada Inválida, Não tem nenhuma peça nessa posição...")
        elif testarSePecaNasCordenadasEhSua(cordenadas, tabuleiro) == False:
            print("! Coordenada Inválida, você não pode mover esta peça..")
        else:
            return True
        return False
    
def testarSeCordenadasSaoValidas(cordenadas:Cordenadas):
    if cordenadas.indice_linha != -1 or cordenadas.indice_coluna != -1:
        return True
    return False

def testarSeExistePecaNasCordenadas(cordenadas:Cordenadas, tabuleiro:list):
    if tabuleiro[cordenadas.indice_linha][cordenadas.indice_coluna] in settings.pecas_jogador_de_brancas or tabuleiro[cordenadas.indice_linha][cordenadas.indice_coluna] in settings.pecas_jogador_de_pretas:
        return True
    return False

def testarSePecaNasCordenadasEhSua(cordenadas:Cordenadas, tabuleiro:list):
    if settings.jogador_atual == Jogador.JOGADOR_DE_BRANCAS:
        if tabuleiro[cordenadas.indice_linha][cordenadas.indice_coluna] in settings.pecas_jogador_de_brancas:
            return True
    elif settings.jogador_atual == Jogador.JOGADOR_DE_PRETAS:
        if tabuleiro[cordenadas.indice_linha][cordenadas.indice_coluna] in settings.pecas_jogador_de_pretas:
            return True
    return False
    
# def testarSePecaPodeIrParaCordenadasFinal(cordenadas_iniciais_validas:Cordenadas, cordenadas_finais_validas:Cordenadas, tabuleiro:list):
    

# def testarValidezCoordenadasFinais(cordenadas_iniciais_validas:Cordenadas, cordenadas_finais:Cordenadas, tabuleiro:list):
#     if testarValidezCoordenadas(cordenadas_finais) == True:
        
#         elif testarValidezCoordenada(cordenadas, tabuleiro) == False:
#             print("! Coordenada Inválida, esta peça não pode ir para esta posição..")
#         elif testarValidezCoordenada(cordenadas, tabuleiro) == False:
#             print("! Coordenada Inválida, você precisa mover a peça para outra posição..")