from settings import settings
from services.tabuleiro import tabuleiros, pecas, movimentos
from models.cords import Cordenadas
from models.enums_utilitarios import StatusDePartida
from services.utilitarios import condicionais_abreviadas as conds
import copy


def testarSeFimDeJogoParaJogadorAtual():
    if testarChequeParaJogadorAtual() == True:
        if testarChequeMateParaJogadorAtual() == True:
            return StatusDePartida.CHEQUE_MATE
        else:
            return StatusDePartida.CHEQUE
    elif testarAfogamentoParaJogadorAtual() == True:
        return StatusDePartida.AFOGAMENTO
    
def testarChequeParaJogadorAtual():
    print("Testando cheque para o jogador atual...")
    for linha, coluna in tabuleiros.percorrerCadaCasaDoTabuleiro():
        peca = pecas.descobrirPeca(Cordenadas(linha, coluna))
        if conds.pecaEhDoJogadorOponente(peca):
            print(f"classe da peca: '{peca.classe}' aparencia: {peca.aparencia} na posição {peca.indice_linha_atual}, {peca.indice_coluna_atual}")
            print(f"classe da peca: '{pecas.descobrirPeca(Cordenadas(1, 5)).classe}' aparencia: {pecas.descobrirPeca(Cordenadas(1, 5)).aparencia}")
            lista_de_movimentos_da_peca = movimentos.descobrirMovimentosValidos(peca)
            for cordenadas in lista_de_movimentos_da_peca:
                print(f"  Testando cheque de {peca.aparencia} para {cordenadas.indice_linha}, {cordenadas.indice_coluna} ocupado por {settings.tabuleiro_principal[cordenadas.indice_linha][cordenadas.indice_coluna].aparencia}")
                if conds.reiEstaAmeaçadoPorMovimento(peca, cordenadas):
                    return True
    return False

def testarChequeMateParaJogadorAtual():
    print("Testando cheque-mate para o jogador atual...")
    if verificarSeChequeAposCadaJogadaPossivel() == True:
        return True
    return False

def testarAfogamentoParaJogadorAtual():
    print("Testando afogamento para o jogador atual...")
    if verificarSeChequeAposCadaJogadaPossivel() == True:
        if testarChequeParaJogadorAtual() == False:
            return True
    return False

def verificarSeChequeAposCadaJogadaPossivel():
    for linha, coluna in tabuleiros.percorrerCadaCasaDoTabuleiro():
        peca = pecas.descobrirPeca(Cordenadas(linha, coluna))
        if conds.pecaEhDoJogadorAtual(peca):
            lista_de_movimentos_da_peca = movimentos.descobrirMovimentosValidos(peca)
            for cordenadas in lista_de_movimentos_da_peca:
                tabuleiro_suporte = copy.deepcopy(settings.tabuleiro_principal)
                movimentos.executarMovimento(peca, cordenadas)
                if testarChequeParaJogadorAtual() == False:
                    tabuleiros.restaurarPosicaoInicialDoTabuleiro(tabuleiro_suporte, peca, Cordenadas(linha, coluna))
                    return False
                tabuleiros.restaurarPosicaoInicialDoTabuleiro(tabuleiro_suporte, peca, Cordenadas(linha, coluna))
    return True

