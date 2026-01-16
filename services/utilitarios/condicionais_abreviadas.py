from settings import settings
from models.enums_utilitarios import Jogador
from models.peca_xadrez import PecaXadrez
from models.cords import Cordenadas


def pecaEhDoJogadorAtual(peca:PecaXadrez):
    if settings.jogador_atual == Jogador.JOGADOR_DE_BRANCAS and peca.aparencia in settings.pecas_jogador_de_brancas or settings.jogador_atual == Jogador.JOGADOR_DE_PRETAS and peca.aparencia in settings.pecas_jogador_de_pretas:
        return True
    return False

def pecaEhDoJogadorOponente(peca:PecaXadrez):
    if settings.jogador_atual == Jogador.JOGADOR_DE_BRANCAS and peca.aparencia in settings.pecas_jogador_de_pretas or settings.jogador_atual == Jogador.JOGADOR_DE_PRETAS and peca.aparencia in settings.pecas_jogador_de_brancas:
        return True
    return False

def jogadorAtualEhDeBrancas():
    if settings.jogador_atual == Jogador.JOGADOR_DE_BRANCAS:
        return True
    return False

def jogadorAtualEhDePretas():
    if settings.jogador_atual == Jogador.JOGADOR_DE_PRETAS:
        return True
    return False

def reiEstaAmeaçadoPorMovimento(peca:PecaXadrez, cordenadas_movimento_possivel:Cordenadas):
    if settings.tabuleiro_principal[cordenadas_movimento_possivel.indice_linha][cordenadas_movimento_possivel.indice_coluna].classe == "rei" and pecaEhDoJogadorOponente(peca):
        print(f"    classe da peça do movimento possível {settings.tabuleiro_principal[cordenadas_movimento_possivel.indice_linha][cordenadas_movimento_possivel.indice_coluna].classe} e peca é do oponente: {pecaEhDoJogadorOponente(peca)}")
        return True
    return False