from enum import Enum

class Jogador(Enum):
    JOGADOR_DE_BRANCAS = 0
    JOGADOR_DE_PRETAS = 1

class StatusDePartida(Enum):
    CHEQUE_MATE = 0
    DESISTENCIA = 1
    AFOGAMENTO = 2
    EMPATE_ACEITO = 3
    CHEQUE = 4
    NORMAL = 5

class TipoDeMovimento(Enum):
    PEAO = 0
    UNICO = 1
    INFINITO = 2

# class TipoDeCordenadaInvalida(Enum):
#     CORDENADAS_DE_TAMANHO_INVALIDO = 0
#     CORDENADAS_DE_FORMATO_INVÁLIDO = 1
#     CORDENADAS_NAO_APONTAM_PARA_PECA = 2
#     CORDENADAS_NAO_APONTAM_PARA_SUA_PECA = 3
#     CORDENADAS_NAO_APONTAM_PARA_MOVIMENTO_POSSIVEL = 4
#     CORDENADAS_INVALIDAS = 5

class TipoDeEntradaInicial(Enum):
    SELECAO_DE_PECA = 0
    SELECAO_E_MOVIMENTO_DE_PECA = 1
    DESISTENCIA = 2
    EMPATE = 3