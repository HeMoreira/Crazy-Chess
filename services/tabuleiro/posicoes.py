from models.cords import Cordenadas
from settings import settings
from services.utilitarios import condicionais_abreviadas as conds
from services.tabuleiro import pecas, movimentos


def converterEntradaEmCordenada(posicoes:str):
    cordenada_y = converterCordenadaY(posicoes[0])
    cordenada_x = converterCordenadaX(posicoes[1])
    cordenadas_da_posicao = Cordenadas(cordenada_x, cordenada_y)
    return cordenadas_da_posicao

def converterCordenadaY(posicao_y:str):
    for chave, valor in settings.conversao_coluna.items():
        if chave == posicao_y:
            return valor-1
    return -1

def converterCordenadaX(posicao_x:str):
    if posicao_x in settings.numeros_tabuleiro:
        return 8-(int(posicao_x))
    return -1

def testarValidezCordenadasDaPeca(cordenadas:Cordenadas):
    if testarSeCordenadasSaoValidas(cordenadas) == False:
        print("! Coordenada Inválida, As cordenadas devem estar entre 'a1' e 'h8'...")
        return False
    else:
        if testarSeExistePecaNasCordenadas(cordenadas) == False:
            print("! Coordenada Inválida, Não tem nenhuma peça nessa posição...")
            return False
        elif testarSePecaNasCordenadasEhSua(cordenadas) == False:
            print("! Coordenada Inválida, você não pode mover esta peça...")
            return False
        return True
    
def testarSeCordenadasSaoValidas(cordenadas:Cordenadas):
    if cordenadas.indice_linha != -1 and cordenadas.indice_coluna != -1:
        return True
    return False

def testarSeExistePecaNasCordenadas(cordenadas:Cordenadas):
    peca = pecas.descobrirPeca(cordenadas)
    if peca.aparencia in settings.pecas_jogador_de_brancas or peca.aparencia in settings.pecas_jogador_de_pretas:
        return True
    return False

def testarSePecaNasCordenadasEhSua(cordenadas:Cordenadas):
    peca = pecas.descobrirPeca(cordenadas)
    if conds.pecaEhDoJogadorAtual(peca) == True:
        return True
    return False

def testarValidezCordenadasDaNovaPosicao(cordenadas_iniciais:Cordenadas, cordenadas_finais:Cordenadas):
    if testarSeCordenadasSaoValidas(cordenadas_finais) == False:
        print("! Coordenada Inválida, As cordenadas devem estar entre 'a1' e 'h8'...")
        return False
    else:
        if testarSeCordenadaFinalNaoEhIgualAInicial(cordenadas_iniciais, cordenadas_finais) == False:
            print("! Coordenada Inválida, você precisa mover a peça para outra posição..")
            return False
        elif testarSePecaPodeIrParaCordenadasFinal(cordenadas_iniciais, cordenadas_finais) == False:
            print("! Coordenada Inválida, esta peça não pode ir para esta posição..")
            return False
        return True

def testarSeCordenadaFinalNaoEhIgualAInicial(cordenadas_iniciais_validas:Cordenadas, cordenadas_finais_validas:Cordenadas):
    if cordenadas_iniciais_validas.indice_linha != cordenadas_finais_validas.indice_linha or cordenadas_iniciais_validas.indice_coluna != cordenadas_finais_validas.indice_coluna:
        return True
    return False

def testarSePecaPodeIrParaCordenadasFinal(cordenadas_iniciais_validas:Cordenadas, cordenadas_finais_validas:Cordenadas):
    peca = pecas.descobrirPeca(cordenadas_iniciais_validas)
    lista_de_movimentos = movimentos.descobrirMovimentosValidos(peca)
    for cordenadas in lista_de_movimentos:
        if cordenadas.indice_linha == cordenadas_finais_validas.indice_linha and cordenadas.indice_coluna == cordenadas_finais_validas.indice_coluna:
            return True
    return False

