from settings import settings
from services.tabuleiro import movimentos, pecas
import copy

def testarCheque():
    # global settings.jogador_atual, settings.partida_rolando, settings.tabuleiro_principal
    for linha in range(8):
        for coluna in range(8):
            peca = pecas.descobrirPeca(linha, coluna)
            if settings.jogador_atual == True and peca.aparencia in "♔♕♖♗♘♙" or settings.jogador_atual == False and peca.aparencia in "♚♛♜♝♞♟":
                if settings.jogador_atual == True:
                    tabuleiro_movimentos = movimentos.descobrirMovimentosValidos(peca, linha, coluna, False)
                else:
                    tabuleiro_movimentos = movimentos.descobrirMovimentosValidos(peca, linha, coluna, True)
                for linha2 in range(8):
                    for coluna2 in range(8):
                        if tabuleiro_movimentos[linha2][coluna2].aparencia == "•":
                            if settings.jogador_atual == True and settings.tabuleiro_principal[linha2][coluna2].aparencia == "♚" or settings.jogador_atual == False and settings.tabuleiro_principal[linha2][coluna2].aparencia == "♔":
                                movimentos.limparMovimentosPossiveis(settings.tabuleiro_principal)
                                return True
    movimentos.limparMovimentosPossiveis(settings.tabuleiro_principal)
    return False

def testarChequeMate():
    # global settings.jogador_atual, settings.partida_rolando, settings.tabuleiro_principal
    em_cheque = True
    quant_movimentos_possiveis = 0
    if testarCheque() == False:
        em_cheque = False
    for linha in range(8):
        for coluna in range(8):
            peca = pecas.descobrirPeca(linha, coluna)
            if settings.jogador_atual == False and peca.aparencia in "♔♕♖♗♘♙" or settings.jogador_atual == True and peca.aparencia in "♚♛♜♝♞♟":
                tabuleiro_movimentos = movimentos.descobrirMovimentosValidos(peca, linha, coluna, settings.jogador_atual)
                for linha2 in range(8):
                    for coluna2 in range(8):
                        if tabuleiro_movimentos[linha2][coluna2].aparencia == "•":
                            movimentos.limparMovimentosPossiveis(settings.tabuleiro_principal)
                            tabuleiro_suporte = copy.deepcopy(settings.tabuleiro_principal)
                            movimentos.executarMovimento(peca, linha, coluna, linha2, coluna2)
                            if testarCheque() == False and em_cheque == False:
                                settings.tabuleiro_principal = copy.deepcopy(tabuleiro_suporte)
                                quant_movimentos_possiveis+=1
                            if testarCheque() == True:
                                settings.tabuleiro_principal = copy.deepcopy(tabuleiro_suporte)
                            elif testarCheque() == False:
                                settings.tabuleiro_principal = copy.deepcopy(tabuleiro_suporte)
                                return "CHEQUE"
    if quant_movimentos_possiveis == 0 and testarCheque() == False:
        return "AFOGAMENTO"
    return "MATE"