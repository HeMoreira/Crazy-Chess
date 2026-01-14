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
    [peca.Torre(False, "♖"), peca.Cavalo(False, "♘"), peca.Bispo(False, "♗"), peca.Rainha(False, "♕"), 
     peca.Rei(False, "♔"), peca.Bispo(False, "♗"), peca.Cavalo(False, "♘"), peca.Torre(False, "♖")],
    [peca.Peao(False, "♙"), peca.Peao(False, "♙"), peca.Peao(False, "♙"), peca.Peao(False, "♙"), 
     peca.Peao(False, "♙"), peca.Peao(False, "♙"), peca.Peao(False, "♙"), peca.Peao(False, "♙")],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, 
     espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, 
     espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, 
     espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, 
     espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [peca.Peao(True, "♟"), peca.Peao(True, "♟"), peca.Peao(True, "♟"), peca.Peao(True, "♟"), 
     peca.Peao(True, "♟"), peca.Peao(True, "♟"), peca.Peao(True, "♟"), peca.Peao(True, "♟")],
    [peca.Torre(True, "♜"), peca.Cavalo(True, "♞"), peca.Bispo(True, "♝"), peca.Rainha(True, "♛"), 
     peca.Rei(True, "♚"), peca.Bispo(True, "♝"), peca.Cavalo(True, "♞"), peca.Torre(True, "♜")]
]

inversao_dinamica_esta_habilitada = True