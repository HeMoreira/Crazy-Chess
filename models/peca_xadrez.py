class pecaXadrez:
    aparencia = ""
    tipos_movimentos = []
    time = True
    se_moveu = False
    tipo_de_movimento = "" #| UNICO | INFINITO | PEAO |
    def __init__(self, tipos_movimentos:list, time:bool, aparencia:str, tipo_de_movimento:str):
        self.aparencia = aparencia
        self.tipos_movimentos = tipos_movimentos
        self.time = time
        self.tipo_de_movimento = tipo_de_movimento

class bispo(pecaXadrez):
    def __init__(self, time:bool, aparencia:str):
        self.time = time
        self.aparencia = aparencia
        self.tipos_movimentos = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
        self.tipo_de_movimento = "INFINITO"

class torre(pecaXadrez):
    def __init__(self, time:bool, aparencia:str):
        self.time = time
        self.aparencia = aparencia
        self.tipos_movimentos = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        self.tipo_de_movimento = "INFINITO"

class rainha(pecaXadrez):
    def __init__(self, time:bool, aparencia:str):
        self.time = time
        self.aparencia = aparencia
        self.tipos_movimentos = [[-1, -1], [-1, 1], [1, -1], [1, 1], [-1, 0], [1, 0], [0, -1], [0, 1]]
        self.tipo_de_movimento = "INFINITO"

class cavalo(pecaXadrez):
    def __init__(self, time:bool, aparencia:str):
        self.time = time
        self.aparencia = aparencia
        self.tipos_movimentos = [[2, -1], [2, 1], [-2, -1], [-2, 1], [-1, 2], [1, 2], [-1, -2], [1, -2]]
        self.tipo_de_movimento = "UNICO"

class peao(pecaXadrez):
    passant_direita = False
    passant_esquerda = False
    promovido = False
    def __init__(self, time:bool, aparencia:str):
        self.time = time
        self.aparencia = aparencia
        if time == False:
            self.tipos_movimentos = [[1, 0], [2, 0], [1, -1], [1, 1]]
        else:
            self.tipos_movimentos = [[-1, 0], [-2, 0], [-1, -1], [-1, 1]]
        self.tipo_de_movimento = "PEAO"

class rei(pecaXadrez):
    def __init__(self, time:bool, aparencia:str):
        self.time = time
        self.aparencia = aparencia
        self.tipos_movimentos = [[-1, -1], [-1, 1], [1, -1], [1, 1], [-1, 0], [1, 0], [0, -1], [0, 1], [0, 2], [0, -2]]
        self.tipo_de_movimento = "UNICO"