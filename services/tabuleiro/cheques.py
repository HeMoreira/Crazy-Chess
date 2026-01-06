from settings import settings
from services.tabuleiro import movimentos, pecas, tabuleiros
from models.enums_utilitarios import Jogador
import copy

def testarChequeParaJogadorAtual():
    for linha, coluna in tabuleiros.percorrerCadaCasaDoTabuleiro():
        peca = pecas.descobrirPeca(linha, coluna)
        if settings.jogador_atual == Jogador.JOGADOR_DE_BRANCAS.value and peca.aparencia in settings.pecas_jogador_de_pretas or settings.jogador_atual == Jogador.JOGADOR_DE_PRETAS.value and peca.aparencia in settings.pecas_jogador_de_brancas:
            tabuleiro_movimentos = movimentos.descobrirMovimentosValidos(peca)
            # TODO: Essa alteração melhora e muito a performance do jogo. Porém, para funcionar, a posição do rei deverá ser atualizada em settings sempre que ele se move.
            if tabuleiro_movimentos[settings.cordenadas_do_rei_branco[0]][settings.cordenadas_do_rei_branco[1]] == "•" and settings.jogador_atual == Jogador.JOGADOR_DE_BRANCAS.value or tabuleiro_movimentos[settings.cordenadas_do_rei_preto[0]][settings.cordenadas_do_rei_preto[1]] == "•" and settings.jogador_atual == Jogador.JOGADOR_DE_PRETAS.value:
                tabuleiros.limparMovimentosPossiveis(settings.tabuleiro_principal)
                return True
    tabuleiros.limparMovimentosPossiveis(settings.tabuleiro_principal)
    return False

def testarSeFimDeJogoParaJogadorAtual():
    if testarChequeParaJogadorAtual() == True:
        if testarChequeMateParaJogadorAtual() == True:
            return "MATE"
        else:
            return "CHEQUE"
    elif testarAfogamentoParaJogadorAtual() == True:
        return "AFOGAMENTO"
    
def testarChequeMateParaJogadorAtual():
    if testarSeChequeAposCadaJogadaPossivel() == True:
        return True
    return False

def testarAfogamentoParaJogadorAtual():
    if testarSeChequeAposCadaJogadaPossivel() == True:
        if testarChequeParaJogadorAtual() == False:
            return True
    return False
        

def testarTodasOsMovimentosPossiveisParaUmaJogada():
    for linha, coluna in tabuleiros.percorrerCadaCasaDoTabuleiro():
        peca = pecas.descobrirPeca(linha, coluna)
        if settings.jogador_atual == Jogador.JOGADOR_DE_PRETAS and peca.aparencia in settings.pecas_jogador_de_pretas or settings.jogador_atual == Jogador.JOGADOR_DE_BRANCAS and peca.aparencia in settings.pecas_jogador_de_brancas:
            tabuleiro_movimentos = movimentos.descobrirMovimentosValidos(peca)
            for linha2, coluna2 in tabuleiros.percorrerCadaCasaDoTabuleiro():
                if tabuleiro_movimentos[linha2][coluna2].aparencia == "•":
                    tabuleiros.limparMovimentosPossiveis(settings.tabuleiro_principal)
                    tabuleiro_suporte = copy.deepcopy(settings.tabuleiro_principal)
                    movimentos.executarMovimento(peca, [linha2, coluna2])
                    yield tabuleiro_suporte

def testarSeChequeAposCadaJogadaPossivel():
    for tabuleiro_suporte in testarTodasOsMovimentosPossiveisParaUmaJogada():
        if testarChequeParaJogadorAtual() == False:
            settings.tabuleiro_principal = copy.deepcopy(tabuleiro_suporte)
            return False
        settings.tabuleiro_principal = copy.deepcopy(tabuleiro_suporte)
    return True