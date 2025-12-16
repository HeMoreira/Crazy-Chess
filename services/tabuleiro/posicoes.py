from settings import settings
from services.tabuleiro import pecas

def descobrirPosicao(coordenadas):
    cord_y = 1000
    for chave, valor in settings.conversao_coluna.items():
        if chave == coordenadas[0]:
            cord_y = valor
    if cord_y == 1000:
        return -1, -1
    cord_x = 100
    if coordenadas[1] in "12345678":
        cord_x = int(coordenadas[1])
    else:
        return -1, -1
    pos1 = 8-(cord_x)
    pos2 = cord_y-1
    return pos1, pos2

def testarValidezCoordenada(entrada, se_nova_posicao, tabuleiro):
    posicao1, posicao2 = descobrirPosicao(entrada)
    if posicao1 == -1:
        return 2
    else:
        peca = None
        peca = tabuleiro[posicao1][posicao2]
        return pecas.testarValidezPeca(peca, se_nova_posicao)
    
def imprimirValidezCoordenada(entrada, se_nova_posicao, tabuleiro):
    if testarValidezCoordenada(entrada, se_nova_posicao, tabuleiro) != 0:
        if testarValidezCoordenada(entrada, se_nova_posicao, tabuleiro) == 1:
            print("! Coordenada Inválida, as coordenadas só podem ter 2 ou 4 caractéres..")
        elif testarValidezCoordenada(entrada, se_nova_posicao, tabuleiro) == 2:
            print("! Coordenada Inválida, digite as coordenadas no formato de [coluna][linha]..")
        elif testarValidezCoordenada(entrada, se_nova_posicao, tabuleiro) == 3:
            print("! Coordenada Inválida, Não tem nenhuma peça nessa posição..")
        elif testarValidezCoordenada(entrada, se_nova_posicao, tabuleiro) == 4:
            print("! Coordenada Inválida, você não pode mover esta peça..")
        elif testarValidezCoordenada(entrada, se_nova_posicao, tabuleiro) == 5:
            print("! Coordenada Inválida, esta peça não pode ir para esta posição..")
        elif testarValidezCoordenada(entrada, se_nova_posicao, tabuleiro) == 6:
            print("! Coordenada Inválida, alguma das informações digitadas não foram aceitas..")
        elif testarValidezCoordenada(entrada, se_nova_posicao, tabuleiro) == 7:
            print("! Coordenada Inválida, você precisa mover a peça para outra posição..")
        else:
            print("! Coordenada Inválida, tipo, ta só errado mesmo ¯\_(ヅ)_/¯")
        return 0
    else:
        return 1