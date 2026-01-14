from models.enums_utilitarios import TipoDeMovimento
from models.enums_utilitarios import Jogador

class PecaXadrez:
    aparencia = ""
    classe = ""
    tipos_movimentos = ()
    time = Jogador.JOGADOR_DE_BRANCAS
    se_moveu = False
    tipo_de_movimento = TipoDeMovimento.INFINITO
    indice_linha_atual = -1
    indice_coluna_atual = -1
    def __init__(self, tipos_movimentos:list, time:bool, aparencia:str, tipo_de_movimento:str, classe:str):
        self.aparencia = aparencia
        self.classe = classe
        self.tipos_movimentos = tipos_movimentos
        self.time = time
        self.tipo_de_movimento = tipo_de_movimento

class Bispo(PecaXadrez):
    def __init__(self, time:bool, aparencia:str, indice_linha_atual:int, indice_coluna_atual:int):
        self.time = time
        self.aparencia = aparencia
        self.classe = "bispo"
        self.tipos_movimentos = ((-1, -1), (1, 1), (1, -1), (1, 1))
        self.tipo_de_movimento = TipoDeMovimento.INFINITO
        self.indice_linha_atual = indice_linha_atual
        self.indice_coluna_atual = indice_coluna_atual

class Torre(PecaXadrez):
    def __init__(self, time:bool, aparencia:str, indice_linha_atual:int, indice_coluna_atual:int):
        self.time = time
        self.aparencia = aparencia
        self.classe = "torre"
        self.tipos_movimentos = ((-1, 0), (1, 0), (0, -1), (0, 1))
        self.tipo_de_movimento = TipoDeMovimento.INFINITO
        self.indice_linha_atual = indice_linha_atual
        self.indice_coluna_atual = indice_coluna_atual

class Rainha(PecaXadrez):
    def __init__(self, time:bool, aparencia:str, indice_linha_atual:int, indice_coluna_atual:int):
        self.time = time
        self.aparencia = aparencia
        self.classe = "rainha"
        self.tipos_movimentos = ((-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1))
        self.tipo_de_movimento = TipoDeMovimento.INFINITO
        self.indice_linha_atual = indice_linha_atual
        self.indice_coluna_atual = indice_coluna_atual

class Cavalo(PecaXadrez):
    def __init__(self, time:bool, aparencia:str, indice_linha_atual:int, indice_coluna_atual:int):
        self.time = time
        self.aparencia = aparencia
        self.classe = "cavalo"
        self.tipos_movimentos = ((2, -1), (2, 1), (-2, -1), (-2, 1), (-1, 2), (1, 2), (-1, -2), (1, -2))
        self.tipo_de_movimento = TipoDeMovimento.UNICO
        self.indice_linha_atual = indice_linha_atual
        self.indice_coluna_atual = indice_coluna_atual

class Peao(PecaXadrez):
    passant_direita = False
    passant_esquerda = False
    promovido = False
    def __init__(self, time:bool, aparencia:str, indice_linha_atual:int, indice_coluna_atual:int):
        self.time = time
        self.aparencia = aparencia
        self.classe = "peao"
        if time == False:
            self.tipos_movimentos = ((1, 0), (2, 0), (1, -1), (1, 1))
        else:
            self.tipos_movimentos = ((-1, 0), (-2, 0), (-1, -1), (-1, 1))
        self.tipo_de_movimento = TipoDeMovimento.PEAO
        self.indice_linha_atual = indice_linha_atual
        self.indice_coluna_atual = indice_coluna_atual

class Rei(PecaXadrez):
    def __init__(self, time:bool, aparencia:str, indice_linha_atual:int, indice_coluna_atual:int):
        self.time = time
        self.aparencia = aparencia
        self.classe = "rei"
        self.tipos_movimentos = ((-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1), (0, 2), (0, -2))
        self.tipo_de_movimento = TipoDeMovimento.UNICO
        self.indice_linha_atual = indice_linha_atual
        self.indice_coluna_atual = indice_coluna_atual