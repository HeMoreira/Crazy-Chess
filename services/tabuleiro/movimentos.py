from models.peca_xadrez import PecaXadrez
from models.enums_utilitarios import TipoDeMovimento, Jogador
from models.cords import Cordenadas
from services.tabuleiro import pecas, tabuleiros, cheques
from services.utilitarios import condicionais_abreviadas as conds
from settings import settings


def descobrirMovimentosValidos(peca:PecaXadrez):
    lista_movimentos_peca = []
    if peca.tipo_de_movimento == TipoDeMovimento.PEAO:
        lista_movimentos_peca = descobrirMovimentosValidosParaPecaTipoPeao(peca)
    elif peca.tipo_de_movimento == TipoDeMovimento.INFINITO:
        lista_movimentos_peca = descobrirMovimentosValidosParaPecaTipoInfinito(peca)
    elif peca.tipo_de_movimento == TipoDeMovimento.UNICO:
        lista_movimentos_peca = descobrirMovimentosValidosParaPecaTipoUnico(peca)
    return lista_movimentos_peca

def descobrirMovimentosValidosParaPecaTipoInfinito(peca:PecaXadrez):
    lista_movimentos_peca = []
    for movimento in peca.tipos_movimentos:
        # o multiplicador testa os movimentos da peça em uma mesma direção até o limite do tabuleiro (8 casas - casa atual)
        for multiplicador in range(1, 8):
            deslocamento_linha = movimento[0] * multiplicador
            deslocamento_coluna = movimento[1] * multiplicador
            possivel_ocupacao_linha = peca.indice_linha_atual + deslocamento_linha
            possivel_ocupacao_coluna = peca.indice_coluna_atual + deslocamento_coluna
            
            possivel_ocupacao = Cordenadas(possivel_ocupacao_linha, possivel_ocupacao_coluna)
        
            if verificarSePossivelOcupacaoEhValida(possivel_ocupacao) == False:
                continue

            lista_movimentos_peca.append(possivel_ocupacao)
    return lista_movimentos_peca

def descobrirMovimentosValidosParaPecaTipoUnico(peca:PecaXadrez):
    lista_movimentos_peca = []
    for movimento in peca.tipos_movimentos:
        deslocamento_linha = movimento[0]
        deslocamento_coluna = movimento[1]
        possivel_ocupacao_linha = peca.indice_linha_atual + deslocamento_linha
        possivel_ocupacao_coluna = peca.indice_coluna_atual + deslocamento_coluna
        possivel_ocupacao = Cordenadas(possivel_ocupacao_linha, possivel_ocupacao_coluna)
        
        if verificarSePossivelOcupacaoEhValida(possivel_ocupacao) == False:
            continue
        if verificarSeRoquePrecisaSerAvaliado(peca, movimento) == True:
            if verificarSeRoqueEhUmaOpcaoValida(peca, movimento) == False:
                continue

        lista_movimentos_peca.append(possivel_ocupacao)
    return lista_movimentos_peca

def verificarSePossivelOcupacaoEhValida(possivel_ocupacao:Cordenadas):
    if verificarSeNovaPosicaoEstaNoTabuleiro(possivel_ocupacao) == True:
        if verificarSeNovaPosicaoEstaLivre(possivel_ocupacao) or verificarSeNovaPosicaoEstaOcupadaPeloTimeInimigo(possivel_ocupacao):
            return True
    return False

def verificarSeNovaPosicaoEstaNoTabuleiro(possivel_ocupacao:Cordenadas):
    if str(possivel_ocupacao.indice_linha) in settings.indices_tabuleiro and str(possivel_ocupacao.indice_coluna) in settings.indices_tabuleiro:
        return True
    return False

def verificarSeNovaPosicaoEstaOcupadaPeloTimeInimigo(possivel_ocupacao:Cordenadas):
    peca_na_posicao_analizada = pecas.descobrirPeca(possivel_ocupacao)
    if conds.pecaEhDoJogadorOponente(peca_na_posicao_analizada):
        return True
    return False

def verificarSeNovaPosicaoEstaLivre(possivel_ocupacao:Cordenadas):
    peca = pecas.descobrirPeca(possivel_ocupacao)
    if peca.classe == "vazio":
        return True
    return False

def verificarSeRoquePrecisaSerAvaliado(peca:PecaXadrez, movimento:list):
    if peca.classe == "rei":
        if movimento == peca.tipos_movimentos[8] or movimento == peca.tipos_movimentos[9]:
            return True
    return False

def verificarSeRoqueEhUmaOpcaoValida(peca:PecaXadrez, movimento:list):
    # Testa se o movimento sendo avaliado é o roque do rei (longo ou curto)
    if peca.classe == "rei" and movimento == peca.tipos_movimentos[8] or peca.classe == "rei" and movimento == peca.tipos_movimentos[9]:
        # Separa a lógica de teste entre roque curto (primeiro) e roque longo (segundo)
        potencial_torre = pecas.descobrirPeca(Cordenadas(peca.indice_linha_atual, 7))
        if peca.classe == "rei" and movimento == peca.tipos_movimentos[8] and potencial_torre.classe == "torre":
            # testa se as condições para o roque são válidas (rei e torre não terem se movido e espaço livre entre as peças)
            if peca.se_moveu == False and potencial_torre.se_moveu == False and potencial_torre.time == peca.time and pecas.descobrirPeca(Cordenadas(peca.indice_linha_atual, 6)).classe == "vazio" and pecas.descobrirPeca(Cordenadas(peca.indice_linha_atual, 5)).classe == "vazio":
                return True
        potencial_torre = pecas.descobrirPeca(Cordenadas(peca.indice_linha_atual, 0))
        if peca.classe == "rei" and movimento == peca.tipos_movimentos[9] and potencial_torre.classe == "torre":
            if peca.se_moveu == False and potencial_torre.se_moveu == False and potencial_torre.time == peca.time and pecas.descobrirPeca(Cordenadas(peca.indice_linha_atual, 1)).classe == "vazio" and pecas.descobrirPeca(Cordenadas(peca.indice_linha_atual, 2)).classe == "vazio" and pecas.descobrirPeca(Cordenadas(peca.indice_linha_atual, 3)).classe == "vazio":
                return True
    return False

def descobrirMovimentosValidosParaPecaTipoPeao(peca:PecaXadrez):
    lista_movimentos_peca = []
    if verificarSePeaoPodeAvancarUmaCasa(peca) == True:
        possivel_ocupacao_linha = peca.indice_linha_atual + peca.tipos_movimentos[0][0]
        lista_movimentos_peca.append(Cordenadas(possivel_ocupacao_linha, peca.indice_coluna_atual))
        if verificarSePeaoPodeAvancarDuasCasas(peca) == True:
            possivel_ocupacao_linha = peca.indice_linha_atual + peca.tipos_movimentos[1][0]
            lista_movimentos_peca.append(Cordenadas(possivel_ocupacao_linha, peca.indice_coluna_atual))

    for i in range(2):
        # representa os movimentos para tomar peças inimigas na diagonal. Para cada valor de i, tratamos de uma diagonal específica
        possivel_ocupacao_linha = peca.indice_linha_atual + peca.tipos_movimentos[2+i][0]
        possivel_ocupacao_coluna = peca.indice_coluna_atual + peca.tipos_movimentos[2+i][1]
        possivel_ocupacao = Cordenadas(possivel_ocupacao_linha, possivel_ocupacao_coluna)

        if verificarSePeaoPodeCapturarEnPassant(peca, i) == True:
            lista_movimentos_peca.append(Cordenadas(possivel_ocupacao_linha, possivel_ocupacao_coluna))
            continue

        if verificarSePeaoPodeAvançarEmDiagonal(possivel_ocupacao) == False:
            continue
        else:
            if verificarSePeaoPodeCapturarEmDiagonal(possivel_ocupacao) == False:
                continue
        lista_movimentos_peca.append(Cordenadas(possivel_ocupacao_linha, possivel_ocupacao_coluna))
    return lista_movimentos_peca

def verificarSePeaoPodeAvancarUmaCasa(peca:PecaXadrez):
    # representa o movimento do peão para 1 casa em sua frente
    possivel_ocupacao_linha = peca.indice_linha_atual + peca.tipos_movimentos[0][0]
    possivel_ocupacao = Cordenadas(possivel_ocupacao_linha, peca.indice_coluna_atual)
    if verificarSePeaoPodeAvancarPara(possivel_ocupacao) == True:
        return True
    return False

def verificarSePeaoPodeAvancarDuasCasas(peca:PecaXadrez):
    # representa o movimento do peão para 1 casa em sua frente
    possivel_ocupacao_linha = peca.indice_linha_atual + peca.tipos_movimentos[1][0]
    possivel_ocupacao = Cordenadas(possivel_ocupacao_linha, peca.indice_coluna_atual)
    if verificarSePeaoPodeAvancarPara(possivel_ocupacao) == True:
        return True
    return False

def verificarSePeaoPodeAvancarPara(possivel_ocupacao:Cordenadas):
    if verificarSeNovaPosicaoEstaNoTabuleiro(possivel_ocupacao) == True:
        if verificarSeNovaPosicaoEstaLivre(possivel_ocupacao) == True:
            return True
    return False

def verificarSePeaoPodeAvançarEmDiagonal(possivel_ocupacao:Cordenadas):
    if str(possivel_ocupacao.indice_linha) in settings.indices_tabuleiro and str(possivel_ocupacao.indice_coluna) in settings.indices_tabuleiro:
        return True
    return False

def verificarSePeaoPodeCapturarEmDiagonal(possivel_ocupacao:Cordenadas):
    peca_na_posicao_analizada = pecas.descobrirPeca(possivel_ocupacao)
    if conds.pecaEhDoJogadorOponente(peca_na_posicao_analizada):
        return True
    return False

def verificarSePeaoPodeCapturarEnPassant(peca:PecaXadrez, i:int):
    if peca.passant_direita == True and i == 1 or peca.passant_esquerda == True and i == 0:
        return True
    return False

def executarMovimento(peca:PecaXadrez, nova_cordenada:Cordenadas):
    
    executarAcoesEspecificasCasoMovimentoSejaEnPassant(peca, nova_cordenada)
    tabuleiros.limparPassantsPossiveis()
    executarAcoesEspecificasCasoMovimentoPermitaNovoEnPassant(peca, nova_cordenada)
    executarAcoesEspecificasCasoMovimentoPromocaoPeao(peca, nova_cordenada)
    executarAcoesEspecificasCasoMovimentoRoque(peca, nova_cordenada)

    executarAcoesGeraisParaQualquerMovimento(peca, nova_cordenada)

def executarAcoesEspecificasCasoMovimentoSejaEnPassant(peca:PecaXadrez, nova_cordenada:Cordenadas):
    if peca.classe == "peao" and nova_cordenada.indice_coluna != peca.indice_coluna_atual and pecas.descobrirPeca(nova_cordenada).classe == "vazio":
        # remover o peão inimigo que foi capturado en passant
        if conds.jogadorAtualEhDeBrancas():
            settings.tabuleiro_principal[nova_cordenada[0]+1][nova_cordenada[1]] = settings.espaco_vazio
        else:
            settings.tabuleiro_principal[nova_cordenada[0]-1][nova_cordenada[1]] = settings.espaco_vazio

def executarAcoesEspecificasCasoMovimentoPermitaNovoEnPassant(peca:PecaXadrez, nova_cordenada:Cordenadas):
    if nova_cordenada.indice_linha - peca.indice_linha_atual in [2, -2] and peca.classe == "peao":
        if nova_cordenada.indice_linha - peca.indice_linha_atual == 2 and nova_cordenada.indice_coluna-1 >= 0:
            if pecas.descobrirPeca(nova_cordenada[0], nova_cordenada[1]-1).aparencia == "♟":
                pecas.descobrirPeca(nova_cordenada[0], nova_cordenada[1]-1).passant_direita = True
        if nova_cordenada.indice_linha - peca.indice_linha_atual == 2 and nova_cordenada.indice_coluna+1 < 8:
            if pecas.descobrirPeca(nova_cordenada[0], nova_cordenada[1]+1).aparencia == "♟":
                pecas.descobrirPeca(nova_cordenada[0], nova_cordenada[1]+1).passant_esquerda = True
        if nova_cordenada.indice_linha - peca.indice_linha_atual == -2 and nova_cordenada.indice_coluna-1 >= 0:
            if pecas.descobrirPeca(nova_cordenada[0], nova_cordenada[1]-1).aparencia == "♙":
                pecas.descobrirPeca(nova_cordenada[0], nova_cordenada[1]-1).passant_direita = True
        if nova_cordenada.indice_linha - peca.indice_linha_atual == -2 and nova_cordenada.indice_coluna+1 < 8:
            if pecas.descobrirPeca(nova_cordenada[0], nova_cordenada[1]+1).aparencia == "♙":
                pecas.descobrirPeca(nova_cordenada[0], nova_cordenada[1]+1).passant_esquerda = True

def executarAcoesEspecificasCasoMovimentoPromocaoPeao(peca:PecaXadrez, nova_cordenada:Cordenadas):
    if peca.aparencia == "♙" and nova_cordenada.indice_linha == 7 or peca.aparencia == "♟" and nova_cordenada.indice_linha == 0:
        peca.promovido = True

def executarAcoesEspecificasCasoMovimentoRoque(peca:PecaXadrez, nova_cordenada:Cordenadas):
    if nova_cordenada.indice_coluna - peca.indice_coluna_atual in [2, -2] and peca.classe == "rei":
        if nova_cordenada.indice_coluna < 4:
            torre = pecas.descobrirPeca(nova_cordenada[0], nova_cordenada[1]-2)
            settings.tabuleiro_principal[nova_cordenada[0]][nova_cordenada[1]+1] = torre
            torre.indice_linha_atual = nova_cordenada[0]
            torre.indice_coluna_atual = nova_cordenada[1]+1

            settings.tabuleiro_principal[nova_cordenada[0]][nova_cordenada[1]-2] = settings.espaco_vazio
        else:
            torre = pecas.descobrirPeca(nova_cordenada[0], nova_cordenada[1]+1)
            settings.tabuleiro_principal[nova_cordenada[0]][nova_cordenada[1]-1] = torre
            torre.indice_linha_atual = nova_cordenada[0]
            torre.indice_coluna_atual = nova_cordenada[1]-1
            
            settings.tabuleiro_principal[nova_cordenada[0]][nova_cordenada[1]+1] = settings.espaco_vazio

def executarAcoesGeraisParaQualquerMovimento(peca:PecaXadrez, nova_cordenada:Cordenadas):
    peca.se_moveu = True
    settings.tabuleiro_principal[nova_cordenada.indice_linha][nova_cordenada.indice_coluna] = peca
    settings.tabuleiro_principal[peca.indice_linha_atual][peca.indice_coluna_atual] = settings.espaco_vazio
    peca.indice_linha_atual = nova_cordenada.indice_linha
    peca.indice_coluna_atual = nova_cordenada.indice_coluna
    if peca.classe == "rei":
        if peca.time == Jogador.JOGADOR_DE_BRANCAS:
            settings.cordenadas_do_rei_branco = [nova_cordenada.indice_linha, nova_cordenada.indice_coluna]
        else:
            settings.cordenadas_do_rei_preto = [nova_cordenada.indice_linha, nova_cordenada.indice_coluna]

def testarSeMovimentoResultaEmCheque():
    if cheques.testarChequeParaJogadorAtual() == True:
        print("Você não pode deixar seu rei ser derrotado.. Faça outro movimento!")
        return True
    return False