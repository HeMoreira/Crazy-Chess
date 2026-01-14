from models import espacos_sem_pecas
from models import peca_xadrez as peca
from models.enums_utilitarios import Jogador

espaco_vazio = espacos_sem_pecas.espacoVazio()
movimento_possivel = espacos_sem_pecas.movimentoPossivel()

pecas_jogador_de_pretas = ["♔", "♕", "♖", "♗", "♘", "♙"]
pecas_jogador_de_brancas = ["♚", "♛", "♜", "♝", "♞", "♟"]
pecas_jogadores = [
    pecas_jogador_de_brancas,
    pecas_jogador_de_pretas
]
espacos_vazios = {
    "espaco vazio":" ",
    "movimento possivel":"•"
}
cordenadas_do_rei_preto = [0, 4]
cordenadas_do_rei_branco = [7, 4]

conversao_coluna = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
numeros_tabuleiro = ("8","7","6","5","4","3","2","1")
indices_tabuleiro = ("0","1","2","3","4","5","6","7")

jogador_atual = Jogador.JOGADOR_DE_BRANCAS
partida_esta_acontecendo = True
rodada_finalizada_com_sucesso = False

tabuleiro_principal = [
    [peca.Torre(False, "♖", 0, 0), peca.Cavalo(False, "♘", 0, 1), peca.Bispo(False, "♗", 0, 2), peca.Rainha(False, "♕", 0, 3), 
     peca.Rei(False, "♔", 0, 4), peca.Bispo(False, "♗", 0, 5), peca.Cavalo(False, "♘", 0, 6), peca.Torre(False, "♖", 0, 7)],
    [peca.Peao(False, "♙", 1, 0), peca.Peao(False, "♙", 1, 1), peca.Peao(False, "♙", 1, 2), peca.Peao(False, "♙", 1, 3), 
     peca.Peao(False, "♙", 1, 4), peca.Peao(False, "♙", 1, 5), peca.Peao(False, "♙", 1, 6), peca.Peao(False, "♙", 1, 7)],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, 
     espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, 
     espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, 
     espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, 
     espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [peca.Peao(True, "♟", 6, 0), peca.Peao(True, "♟", 6, 1), peca.Peao(True, "♟", 6, 2), peca.Peao(True, "♟", 6, 3), 
     peca.Peao(True, "♟", 6, 4), peca.Peao(True, "♟", 6, 5), peca.Peao(True, "♟", 6, 6), peca.Peao(True, "♟", 6, 7)],
    [peca.Torre(True, "♜", 7, 0), peca.Cavalo(True, "♞", 7, 1), peca.Bispo(True, "♝", 7, 2), peca.Rainha(True, "♛", 7, 3), 
     peca.Rei(True, "♚", 7, 4), peca.Bispo(True, "♝", 7, 5), peca.Cavalo(True, "♞", 7, 6), peca.Torre(True, "♜", 7, 7)]
]

inversao_dinamica_esta_habilitada = False