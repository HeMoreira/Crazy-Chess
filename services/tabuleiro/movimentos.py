from settings import settings
from services.tabuleiro import tabuleiros, pecas

def descobrirMovimentosValidos(peca, posicao1, posicao2, jogador):
    tabuleiro_movimentos = tabuleiros.novoTabuleiroVazio()
    if peca.tipo_de_movimento == "PEAO":

        teste_movimento = posicao1 + peca.tipos_movimentos[0][0]
        if str(teste_movimento) in "01234567" and settings.tabuleiro_principal[teste_movimento][posicao2].aparencia in "• ":
            possivel_ocupacao_linha = posicao1 + peca.tipos_movimentos[0][0]
            possivel_ocupacao_coluna = posicao2 + peca.tipos_movimentos[0][1]
            settings.tabuleiro_principal[possivel_ocupacao_linha][possivel_ocupacao_coluna] = settings.movimento_possivel
            tabuleiro_movimentos[possivel_ocupacao_linha][possivel_ocupacao_coluna] = settings.movimento_possivel

            teste_movimento = posicao1 + peca.tipos_movimentos[1][0]
            if str(teste_movimento) in "01234567" and str(posicao1) in "16" and settings.tabuleiro_principal[teste_movimento][posicao2].aparencia in "• ":
                possivel_ocupacao_linha = posicao1 + peca.tipos_movimentos[1][0]
                possivel_ocupacao_coluna = posicao2 + peca.tipos_movimentos[1][1]
                settings.tabuleiro_principal[possivel_ocupacao_linha][possivel_ocupacao_coluna] = settings.movimento_possivel
                tabuleiro_movimentos[possivel_ocupacao_linha][possivel_ocupacao_coluna] = settings.movimento_possivel

        for c in range(2):
            teste_movimento1 = posicao1 + peca.tipos_movimentos[2+c][0]
            teste_movimento2 = posicao2 + peca.tipos_movimentos[2+c][1]
            if str(teste_movimento1) not in "01234567" or str(teste_movimento2) not in "01234567":
                continue
            elif jogador == True and pecas.descobrirPeca(teste_movimento1, teste_movimento2).aparencia in "♔♕♖♗♘♙" and settings.tabuleiro_principal[teste_movimento1][teste_movimento2].aparencia != "":
                tabuleiro_movimentos[teste_movimento1][teste_movimento2] = settings.movimento_possivel
                continue
            elif jogador == False and pecas.descobrirPeca(teste_movimento1, teste_movimento2).aparencia in "♚♛♜♝♞♟" and settings.tabuleiro_principal[teste_movimento1][teste_movimento2].aparencia != "":
                tabuleiro_movimentos[teste_movimento1][teste_movimento2] = settings.movimento_possivel
                continue
            elif pecas.descobrirPeca(posicao1, posicao2).passant_direita == True and c == 1 or pecas.descobrirPeca(posicao1, posicao2).passant_esquerda == True and c == 0:
                tabuleiro_movimentos[teste_movimento1][teste_movimento2] = settings.movimento_possivel
                settings.tabuleiro_principal[teste_movimento1][teste_movimento2] = settings.movimento_possivel
                continue

    else:
        for movimento in peca.tipos_movimentos:
            for multiplicador in range(10):
                if peca.tipo_de_movimento == "INFINITO":
                    possivel_ocupacao_linha = posicao1 + movimento[0]*(multiplicador+1)
                    possivel_ocupacao_coluna = posicao2 + movimento[1]*(multiplicador+1)
                elif peca.tipo_de_movimento == "UNICO":
                    possivel_ocupacao_linha = posicao1 + movimento[0]
                    possivel_ocupacao_coluna = posicao2 + movimento[1]
                if str(possivel_ocupacao_linha) not in "01234567" or str(possivel_ocupacao_coluna) not in "01234567":
                    break
                elif peca.aparencia in "♔♚" and movimento == peca.tipos_movimentos[8] or peca.aparencia in "♔♚" and movimento == peca.tipos_movimentos[9]:
                    if peca.aparencia in "♔♚" and movimento == peca.tipos_movimentos[8] and pecas.descobrirPeca(posicao1, 7).aparencia in "♖♜":
                        if peca.se_moveu == False and pecas.descobrirPeca(posicao1, 7).se_moveu == False and pecas.descobrirPeca(posicao1, 7).time == peca.time and pecas.descobrirPeca(posicao1, 6).aparencia in "• " and pecas.descobrirPeca(posicao1, 5).aparencia in "• ":
                            settings.tabuleiro_principal[possivel_ocupacao_linha][possivel_ocupacao_coluna] = settings.movimento_possivel
                            tabuleiro_movimentos[possivel_ocupacao_linha][possivel_ocupacao_coluna] = settings.movimento_possivel
                    if peca.aparencia in "♔♚" and movimento == peca.tipos_movimentos[9] and pecas.descobrirPeca(posicao1, 0).aparencia in "♖♜":
                        if peca.se_moveu == False and pecas.descobrirPeca(posicao1, 0).se_moveu == False and pecas.descobrirPeca(posicao1, 0).time == peca.time and pecas.descobrirPeca(posicao1, 1).aparencia in "• " and pecas.descobrirPeca(posicao1, 2).aparencia in "• " and pecas.descobrirPeca(posicao1, 3).aparencia in "• ":
                            settings.tabuleiro_principal[possivel_ocupacao_linha][possivel_ocupacao_coluna] = settings.movimento_possivel
                            tabuleiro_movimentos[possivel_ocupacao_linha][possivel_ocupacao_coluna] = settings.movimento_possivel
                    break
                elif pecas.descobrirPeca(possivel_ocupacao_linha, possivel_ocupacao_coluna).aparencia in "• ":
                    settings.tabuleiro_principal[possivel_ocupacao_linha][possivel_ocupacao_coluna] = settings.movimento_possivel
                    tabuleiro_movimentos[possivel_ocupacao_linha][possivel_ocupacao_coluna] = settings.movimento_possivel
                elif pecas.descobrirPeca(possivel_ocupacao_linha, possivel_ocupacao_coluna).aparencia in "♔♕♖♗♘♙" and pecas.descobrirPeca(possivel_ocupacao_linha, possivel_ocupacao_coluna).aparencia != "" and jogador == True or pecas.descobrirPeca(possivel_ocupacao_linha, possivel_ocupacao_coluna).aparencia in "♚♛♜♝♞♟" and pecas.descobrirPeca(possivel_ocupacao_linha, possivel_ocupacao_coluna).aparencia != "" and jogador == False:
                    tabuleiro_movimentos[possivel_ocupacao_linha][possivel_ocupacao_coluna] = settings.movimento_possivel
                    break
                else:
                    break
    return tabuleiro_movimentos

def mostrarMovimentosValidos(peca, posicao1, posicao2, jogador):
    tabuleiro_movimentos = []
    for c in range(8):
        for i in range(8):
            if peca == settings.tabuleiro_principal[c][i]:
                tabuleiro_movimentos = descobrirMovimentosValidos(peca, posicao1, posicao2, jogador)
    return tabuleiro_movimentos

def executarMovimento(peca, pos1, pos2, n_pos1, n_pos2):

    #execução caso o movimento escolhido seja de fato o en passant
    if settings.tabuleiro_principal[n_pos1][n_pos2].aparencia == "•" and n_pos2 != pos2 and peca.aparencia in "♙♟":
        if settings.jogador_atual == True:
            settings.tabuleiro_principal[n_pos1+1][n_pos2] = settings.espaco_vazio
        else:
            settings.tabuleiro_principal[n_pos1-1][n_pos2] = settings.espaco_vazio
            
    limparPassantsPossiveis(settings.tabuleiro_principal)

    #execução caso en passant seja possivel
    if n_pos1 - pos1 == 2 and peca.aparencia == "♙" or n_pos1 - pos1 == -2 and peca.aparencia == "♟":
        if n_pos1 - pos1 == 2 and n_pos2-1 >= 0:
            if pecas.descobrirPeca(n_pos1, n_pos2-1).aparencia == "♟":
                pecas.descobrirPeca(n_pos1, n_pos2-1).passant_direita = True
        if n_pos1 - pos1 == 2 and n_pos2+1 < 8:
            if pecas.descobrirPeca(n_pos1, n_pos2+1).aparencia == "♟":
                pecas.descobrirPeca(n_pos1, n_pos2+1).passant_esquerda = True
        if n_pos1 - pos1 == -2 and n_pos2-1 >= 0:
            if pecas.descobrirPeca(n_pos1, n_pos2-1).aparencia == "♙":
                pecas.descobrirPeca(n_pos1, n_pos2-1).passant_direita = True
        if n_pos1 - pos1 == -2 and n_pos2+1 < 8:
            if pecas.descobrirPeca(n_pos1, n_pos2+1).aparencia == "♙":
                pecas.descobrirPeca(n_pos1, n_pos2+1).passant_esquerda = True

    #execução caso o peão movido esteja na linha de promoção
    if peca.aparencia == "♙" and n_pos1 == 7 or peca.aparencia == "♟" and n_pos1 == 0:
        peca.promovido = True

    #execução caso roque
    elif n_pos2 - pos2 == 2 and peca.aparencia in "♔♚" and peca.se_moveu == False or n_pos2 - pos2 == -2 and peca.aparencia in "♔♚" and peca.se_moveu == False:
        if n_pos2 < 4:
            settings.tabuleiro_principal[n_pos1][n_pos2+1] = settings.tabuleiro_principal[n_pos1][n_pos2-2]
            settings.tabuleiro_principal[n_pos1][n_pos2-2] = settings.espaco_vazio
        else:
            settings.tabuleiro_principal[n_pos1][n_pos2-1] = settings.tabuleiro_principal[n_pos1][n_pos2+1]
            settings.tabuleiro_principal[n_pos1][n_pos2+1] = settings.espaco_vazio
            

    #execução padrão e geral do movimento
    peca.se_moveu = True
    settings.tabuleiro_principal[n_pos1][n_pos2] = peca
    settings.tabuleiro_principal[pos1][pos2] = settings.espaco_vazio

def limparMovimentosPossiveis(tabuleiro):
    for linha in range(8):
        for coluna in range(8):
            if tabuleiro[linha][coluna].aparencia == "•":
                tabuleiro[linha][coluna] = settings.espaco_vazio

def limparPassantsPossiveis(tabuleiro):
    for linha in range(8):
        for coluna in range(8):
            if tabuleiro[linha][coluna].aparencia in "♟♙":
                tabuleiro[linha][coluna].passant_direita = False
                tabuleiro[linha][coluna].passant_esquerda = False