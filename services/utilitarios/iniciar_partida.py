from services.utilitarios import impressoes, turnos, condicionais_abreviadas as conds
from settings import settings
from models.enums_utilitarios import Jogador

def iniciarPartida():
    impressoes.introduzirPartida()
    settings.jogador_atual = Jogador.JOGADOR_DE_PRETAS
    settings.partida_esta_acontecendo = True
    while settings.partida_esta_acontecendo:
        turnos.executarTurnoAtual()
        passarVez()

def passarVez():
    if conds.jogadorAtualEhDeBrancas():
        settings.jogador_atual = Jogador.JOGADOR_DE_PRETAS
    elif conds.jogadorAtualEhDePretas():
        settings.jogador_atual = Jogador.JOGADOR_DE_BRANCAS