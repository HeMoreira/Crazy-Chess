from services.utilitarios import impressoes
from services.tabuleiro import tabuleiros
from settings import settings
from models.enums_utilitarios import StatusDePartida, Jogador


def fimDeJogo(razao:StatusDePartida):
    match razao:
        case StatusDePartida.DESISTENCIA:
            if settings.jogador_atual == Jogador.JOGADOR_DE_BRANCAS:
                impressoes.imprimirCabecalhoComSubtitulo("FIM DE JOGO..", "As Brancas desistiram, a vitória é das Pretas!! ♔")
            elif settings.jogador_atual == Jogador.JOGADOR_DE_PRETAS:
                impressoes.imprimirCabecalhoComSubtitulo("FIM DE JOGO..", "As Pretas desistiram, a vitória é das Brancas!! ♚")
            settings.partida_esta_acontecendo = False
        case StatusDePartida.CHEQUE_MATE:
            impressoes.imprimirCabecalhoComSubtitulo("! CHEQUE MATE !", "Seu rei foi encurralado, esse é o fim para você..")
            tabuleiros.imprimirTabuleiro()
            if settings.jogador_atual == Jogador.JOGADOR_DE_BRANCAS:
                impressoes.imprimirCabecalhoComSubtitulo("FIM DE JOGO..", "O rei Branco foi encurralado, Pretas Venceram!! ♔")
            elif settings.jogador_atual == Jogador.JOGADOR_DE_PRETAS:
                impressoes.imprimirCabecalhoComSubtitulo("FIM DE JOGO..", "O rei Preto foi encurralado, Brancas Venceram!! ♚")
            settings.partida_esta_acontecendo = False
        case StatusDePartida.AFOGAMENTO:
            impressoes.imprimirCabecalhoComSubtitulo("! AFOGAMENTO !", "Você não é capaz de passar a vez, empate forçado!")
            tabuleiros.imprimirTabuleiro()
            impressoes.imprimirCabecalhoComSubtitulo("FIM DE JOGO..", "Um dos jogadores não pode se mover, empate forçado! #")
            settings.partida_esta_acontecendo = False
        case StatusDePartida.EMPATE_ACEITO:
            impressoes.imprimirCabecalhoComSubtitulo("FIM DE JOGO..", "Que partida! Os jogadores negociaram um empate! #")
            settings.partida_esta_acontecendo = False

def tentarPedidoPorEmpate():
    impressoes.imprimirCabecalhoComSubtitulo("! PROPOSTA DE EMPATE !", "Seu oponente propôs empate, você aceita?")
    resposta = "resposta inválida"
    while resposta.lower() != "sim" and resposta.lower() != "nao" and resposta.lower() != "não":
        resposta = input("Responda 'SIM' ou 'NÃO' conforme a sua resposta\nResposta: ")
    if resposta.lower() == "sim":
        return True
    else:
        return False