from settings import settings
from services.utilitarios import turno_atual

def introducaoPartida():
    print("Que começem os Jogos..") 
    print("=====================================================") 
    print("-=             PARTIDA PADRÃO DE XADREZ            =-") 
    print("=====================================================")
    print("\n")
    # global settings.partida_rolando, settings.partida_rolando
    settings.partida_rolando = True
    settings.jogador_atual = True
    turno_atual.turnoAtual(settings.jogador_atual)

    