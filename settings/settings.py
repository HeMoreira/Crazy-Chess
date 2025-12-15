from models import espacos_sem_pecas, peca_xadrez

peca = peca_xadrez
espaco_vazio = espacos_sem_pecas.espacoVazio()
movimento_possivel = espacos_sem_pecas.movimentoPossivel()

numeros_tabuleiro = ["8","7","6","5","4","3","2","1"]
conversao_coluna = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}

#"""
tabuleiro_principal = [
    [peca.torre(False, "♖"), peca.cavalo(False, "♘"), peca.bispo(False, "♗"), peca.rainha(False, "♕"), peca.rei(False, "♔"), peca.bispo(False, "♗"), peca.cavalo(False, "♘"), peca.torre(False, "♖")],
    [peca.peao(False, "♙"), peca.peao(False, "♙"), peca.peao(False, "♙"), peca.peao(False, "♙"), peca.peao(False, "♙"), peca.peao(False, "♙"), peca.peao(False, "♙"), peca.peao(False, "♙")],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [peca.peao(True, "♟"), peca.peao(True, "♟"), peca.peao(True, "♟"), peca.peao(True, "♟"), peca.peao(True, "♟"), peca.peao(True, "♟"), peca.peao(True, "♟"), peca.peao(True, "♟")],
    [peca.torre(True, "♜"), peca.cavalo(True, "♞"), peca.bispo(True, "♝"), peca.rainha(True, "♛"), peca.rei(True, "♚"), peca.bispo(True, "♝"), peca.cavalo(True, "♞"), peca.torre(True, "♜")]
]
"""
tabuleiro_principal = [
    [peca.torre(False, "♖"), peca.cavalo(False, "♘"), peca.bispo(False, "♗"), peca.rainha(False, "♕"), peca.rei(False, "♔"), peca.bispo(False, "♗"), peca.cavalo(False, "♘"), peca.torre(False, "♖")],
    [peca.peao(False, "♙"), peca.peao(False, "♙"), peca.peao(False, "♙"), peca.peao(False, "♙"), peca.peao(False, "♙"), peca.peao(False, "♙"), peca.peao(False, "♙"), peca.peao(False, "♙")],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [peca.peao(True, "♟"), peca.peao(True, "♟"), peca.peao(True, "♟"), peca.peao(True, "♟"), peca.peao(True, "♟"), peca.peao(True, "♟"), peca.peao(True, "♟"), peca.peao(True, "♟")],
    [peca.torre(True, "♜"), peca.cavalo(True, "♞"), peca.bispo(True, "♝"), peca.rainha(True, "♛"), peca.rei(True, "♚"), peca.bispo(True, "♝"), peca.cavalo(True, "♞"), peca.torre(True, "♜")]
]
#"""

#BRANCAS = TRUE, PRETAS = FALSE
partida_rolando = True
jogador_atual = True