from models import espacos_sem_pecas
from models import peca_xadrez as peca
from models.enums_utilitarios import Jogador

espaco_vazio = espacos_sem_pecas.espacoVazio()
movimento_possivel = espacos_sem_pecas.movimentoPossivel()

pecas_jogador_de_pretas = ["♔", "♕", "♖", "♗", "♘", "♙"]
pecas_jogador_de_brancas = ["♚", "♛", "♜", "♝", "♞", "♟"]
pecas_jogadores = [
    pecas_jogador_de_pretas,
    pecas_jogador_de_brancas
]
espacos_vazios = {
    "espaco vazio":" ",
    "movimento possivel":"•"
}

conversao_coluna = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
numeros_tabuleiro = ("8","7","6","5","4","3","2","1")
indices_tabuleiro = ("0","1","2","3","4","5","6","7")

jogador_atual = Jogador.JOGADOR_DE_BRANCAS
partida_esta_acontecendo = True
rodada_finalizada_com_sucesso = False

#"""
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
"""
tabuleiro_principal = [
    [peca.Torre(False, "♖", 0, 0), peca.Cavalo(False, "♘", 0, 1), peca.Bispo(False, "♗", 0, 2), peca.Rainha(False, "♕", 0, 3), 
     peca.Rei(False, "♔", 0, 4), peca.Bispo(False, "♗", 0, 5), peca.Cavalo(False, "♘", 0, 6), peca.Torre(False, "♖", 0, 7)],
    [peca.Peao(False, "♙", 1, 0), peca.Peao(False, "♙", 1, 1), peca.Peao(False, "♙", 1, 2), peca.Peao(False, "♙", 1, 3), 
     espaco_vazio, peca.Rainha(True, "♛", 1, 5), peca.Peao(False, "♙", 1, 6), peca.Peao(False, "♙", 1, 7)],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, 
     espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, 
     peca.Peao(False, "♙", 3, 4), espaco_vazio, espaco_vazio, espaco_vazio],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, 
     peca.Peao(True, "♟", 4, 4), espaco_vazio, espaco_vazio, espaco_vazio],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, 
     espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [peca.Peao(True, "♟", 6, 0), peca.Peao(True, "♟", 6, 1), peca.Peao(True, "♟", 6, 2), peca.Peao(True, "♟", 6, 3), 
     espaco_vazio, peca.Peao(True, "♟", 6, 5), peca.Peao(True, "♟", 6, 6), peca.Peao(True, "♟", 6, 7)],
    [peca.Torre(True, "♜", 7, 0), peca.Cavalo(True, "♞", 7, 1), peca.Bispo(True, "♝", 7, 2), espaco_vazio, 
     peca.Rei(True, "♚", 7, 4), peca.Bispo(True, "♝", 7, 5), peca.Cavalo(True, "♞", 7, 6), peca.Torre(True, "♜", 7, 7)]
]
#"""
inversao_dinamica_esta_habilitada = False

respostas_teste = "1\ne2e4\n\ne7e5\n\ng1f3\n\nb8c6\n\nc2c3\n\nf7f6\n\nf1\nb5\n\nf8c5\n\nd2d4\n\ne5d4\n\nc3d4\n\nc5d4\n\nf3d4\n\nc6d4\n\nd1d4\n\nempate\nnao\ne8f7\n\nc1\ntrocar\ne1g1\n\nc7c6\n\nb5a4\n\nb7b5\n\na4b3\n\nf7f8\n\nc1e3\n\ng8e7\n\nb1c3\n\nf6f5\n\ne4f5\n\ne7f5\n\nd4f4\n\nf8e8\n\nf4f5\n\nd8f6\n\nf5f6\n\ng7g6\ncancelar\ng7f6\n\ne3\nh6\n\nh7d5\nc3d5\nd7d5\n\nc3d5\n\nc6d5\n\nb3d5\n\ne8\ntrocar\na8b8\n\na2a3\n\nf6f5\n\nb2b4\n\nc8b7\n\nd5b3\n\nb7e4\n\na1d1\n\nb8d8\n\nd1d2\n\nf5f4\n\ng2g44\ng2g4\n\nf4g3\n\nh2g3\n\ne4d5\n\nb3d5\n\nd8d5\n\nd2d5\n\ne8f7\n\nf1e1\n\nh8e8\n\ne1e8\n\nf7e8\n\nd5b5\n\nempate\nnaop\nNAO\ne8f7\n\nb5b7\n\nf7g6\n\nh6f8\n\nh7h5\n\nb7a7\n\ng6g5\n\nf2f3\n\nh5h4\n\ng3h4\n\ng5h4\n\ng1g2\n\nh4h5\n\ng2g3\n\nh5h6\n\nh5g6\n\ng3g4\n\ng6f6\n\na7c7\n\nf6e5\n\nc7c4\n\ne5d5\n\nb4b5\n\nd5c4\n\nb5b6\n\nc4b5\n\nb6b7\n\nb5a4\n\nb7b8\ntorre\ncancelar\nb7b8\nrainha\n\na4a5\n\nb8a7\n\na5b5\n\na7c5\n\nempate\nnao\nb5a4\n\nc5b6\n\n"