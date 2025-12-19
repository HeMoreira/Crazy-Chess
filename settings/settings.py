from models import espacos_sem_pecas, peca_xadrez
from models.enums_utilitarios import Jogador

espaco_vazio = espacos_sem_pecas.espacoVazio()
movimento_possivel = espacos_sem_pecas.movimentoPossivel()

pecas_jogador_de_pretas = {
    "rei":"♔",
    "rainha":"♕",
    "torre":"♖",
    "bispo":"♗",
    "cavalo":"♘",
    "peao":"♙"
}
pecas_jogador_de_brancas = {
    "rei":"♚",
    "rainha":"♛",
    "torre":"♜",
    "bispo":"♝",
    "cavalo":"♞",
    "peao":"♟"
}
espacos_vazios = {
    "espaco vazio":" ",
    "movimento possivel":"•"
}

conversao_coluna = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
numeros_tabuleiro = ("8","7","6","5","4","3","2","1")
indices_tabuleiro = ("0","1","2","3","4","5","6","7")

jogador_atual = Jogador.JOGADOR_DE_BRANCAS
partida_rolando = True

tabuleiro_principal = [
    [peca_xadrez.torre(False, "♖"), peca_xadrez.cavalo(False, "♘"), 
     peca_xadrez.bispo(False, "♗"), peca_xadrez.rainha(False, "♕"), 
     peca_xadrez.rei(False, "♔"), peca_xadrez.bispo(False, "♗"), 
     peca_xadrez.cavalo(False, "♘"), peca_xadrez.torre(False, "♖")],
    [peca_xadrez.peao(False, "♙"), peca_xadrez.peao(False, "♙"), 
     peca_xadrez.peao(False, "♙"), peca_xadrez.peao(False, "♙"), 
     peca_xadrez.peao(False, "♙"), peca_xadrez.peao(False, "♙"), 
     peca_xadrez.peao(False, "♙"), peca_xadrez.peao(False, "♙")],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, 
     espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, 
     espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, 
     espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, 
     espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [peca_xadrez.peao(True, "♟"), peca_xadrez.peao(True, "♟"), 
     peca_xadrez.peao(True, "♟"), peca_xadrez.peao(True, "♟"), 
     peca_xadrez.peao(True, "♟"), peca_xadrez.peao(True, "♟"), 
     peca_xadrez.peao(True, "♟"), peca_xadrez.peao(True, "♟")],
    [peca_xadrez.torre(True, "♜"), peca_xadrez.cavalo(True, "♞"), 
     peca_xadrez.bispo(True, "♝"), peca_xadrez.rainha(True, "♛"), 
     peca_xadrez.rei(True, "♚"), peca_xadrez.bispo(True, "♝"), 
     peca_xadrez.cavalo(True, "♞"), peca_xadrez.torre(True, "♜")]
]

inversao_dinamica_esta_habilitada = True