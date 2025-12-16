from settings import settings
from services.tabuleiro import tabuleiros

def descobrirPeca(posicao1, posicao2):
    return settings.tabuleiro_principal[posicao1][posicao2]

def testarValidezPeca(peca, se_nova_posicao):
    if peca.aparencia == " " and se_nova_posicao == False:
        return 3
    elif peca.aparencia in "♔♕♖♗♘♙" and peca.aparencia != "" and settings.jogador_atual == True and se_nova_posicao == False:
        return 4
    elif peca.aparencia in "♚♛♜♝♞♟" and peca.aparencia != "" and settings.jogador_atual == False and se_nova_posicao == False:
        return 4
    elif se_nova_posicao == True and peca.aparencia != "•":
        return 5
    else:
        return 0
    
def PromoverPeao(peca, pos1, pos2):
    print("=====================================================")
    print("                -= PROMOÇÃO DE PEÃO =-               ")
    print("=====================================================")
    tabuleiros.imprimirTabuleiro(settings.tabuleiro_principal)
    print("=====================================================")
    print("Que aventura em.. deseja trocar seu peão por qual peça?\nVocê pode escolher entre 'cavalo', 'torre', 'bispo', e 'rainha'")
    promocao = "aaaaaaaaaaaa"
    while promocao != "cavalo" and promocao != "bispo" and promocao != "torre" and promocao != "rainha":
        promocao = input("Resposta: ")
        promocao = promocao.lower()
        if promocao == "cavalo":
            if peca.time == True:
                settings.tabuleiro_principal[pos1][pos2] = settings.peca.cavalo(True, "♞")
            else:
                settings.tabuleiro_principal[pos1][pos2] = settings.peca.cavalo(False, "♘")
        elif promocao == "torre":
            if peca.time == True:
                settings.tabuleiro_principal[pos1][pos2] = settings.peca.torre(True, "♜")
            else:
                settings.tabuleiro_principal[pos1][pos2] = settings.peca.torre(False, "♖")
        elif promocao == "bispo":
            if peca.time == True:
                settings.tabuleiro_principal[pos1][pos2] = settings.peca.bispo(True, "♝")
            else:
                settings.tabuleiro_principal[pos1][pos2] = settings.peca.bispo(False, "♗")
        elif promocao == "rainha":
            if peca.time == True:
                settings.tabuleiro_principal[pos1][pos2] = settings.peca.rainha(True, "♛")
            else:
                settings.tabuleiro_principal[pos1][pos2] = settings.peca.rainha(False, "♕")
        else:
            print("! Entrada Inválida, certifique-se de escrever o nome correto da peça...")
    print("=====================================================")
    print(f"{settings.tabuleiro_principal[pos1][pos2].aparencia} - Seu peão foi promovido para {promocao}!!")
    print("=====================================================")