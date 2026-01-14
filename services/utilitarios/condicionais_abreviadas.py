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
    if cordenadas_movimento_possivel.indice_linha == settings.cordenadas_do_rei_branco[0] and cordenadas_movimento_possivel.indice_coluna == settings.cordenadas_do_rei_branco[1] and peca.time == Jogador.JOGADOR_DE_PRETAS or cordenadas_movimento_possivel.indice_linha == settings.cordenadas_do_rei_preto[0] and cordenadas_movimento_possivel.indice_coluna == settings.cordenadas_do_rei_preto[1] and peca.time == Jogador.JOGADOR_DE_BRANCAS:
        return True
    return False