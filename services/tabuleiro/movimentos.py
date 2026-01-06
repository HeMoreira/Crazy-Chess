from settings import settings
from services.tabuleiro import tabuleiros, pecas
from models.cords import Cordenadas
from models.enums_utilitarios import TipoDeMovimento, Jogador
from models.peca_xadrez import PecaXadrez

def descobrirMovimentosValidos(peca:PecaXadrez):
    tabuleiro_movimentos = tabuleiros.criarNovoTabuleiroVazio()
    if peca.tipo_de_movimento == TipoDeMovimento.PEAO.value:
        descobrirMovimentosValidosParaPecaTipoPeao(peca, tabuleiro_movimentos)
    elif peca.tipo_de_movimento == TipoDeMovimento.INFINITO.value:
        descobrirMovimentosValidosParaPecaTipoInfinito(peca, tabuleiro_movimentos)
    elif peca.tipo_de_movimento == TipoDeMovimento.UNICO.value:
        descobrirMovimentosValidosParaPecaTipoUnico(peca, tabuleiro_movimentos)
    return tabuleiro_movimentos

def descobrirMovimentosValidosParaPecaTipoUnico(peca:PecaXadrez, tabuleiro_movimentos:list):
    for movimento in peca.tipos_movimentos:
        possivel_ocupacao_linha = peca.indice_linha_atual + movimento[0]
        possivel_ocupacao_coluna = peca.indice_coluna_atual + movimento[1]
        possivel_ocupacao = Cordenadas(possivel_ocupacao_linha, possivel_ocupacao_coluna)
        
        if testarSePossivelOcupacaoEhValida(possivel_ocupacao) == False:
            continue

        if verificarSeRoqueEhUmaOpcaoValida(peca, movimento, tabuleiro_movimentos) == True:
            continue
        elif verificarSeNovaPosicaoEstaLivre(possivel_ocupacao, tabuleiro_movimentos) == True:
            continue
        verificarSeNovaPosicaoEstaOcupadaPeloTimeInimigo(possivel_ocupacao, tabuleiro_movimentos)
        # se não for, certamente é uma peça do seu time, dispensando qualquer ação

def descobrirMovimentosValidosParaPecaTipoInfinito(peca:PecaXadrez, tabuleiro_movimentos:list):
    for movimento in peca.tipos_movimentos:
        for multiplicador in range(10):
            possivel_ocupacao_linha = peca.indice_linha_atual + movimento[0]*(multiplicador+1)
            possivel_ocupacao_coluna = peca.indice_coluna_atual + movimento[1]*(multiplicador+1)
            possivel_ocupacao = Cordenadas(possivel_ocupacao_linha, possivel_ocupacao_coluna)
        
            if testarSePossivelOcupacaoEhValida(possivel_ocupacao) == False:
                continue

            if verificarSeNovaPosicaoEstaLivre(possivel_ocupacao, tabuleiro_movimentos) == True:
                continue
            elif verificarSeNovaPosicaoEstaOcupadaPeloTimeInimigo(possivel_ocupacao, tabuleiro_movimentos) == True:
                break
            # se não for, certamente é uma peça do seu time, dispensando qualquer ação

def descobrirMovimentosValidosParaPecaTipoPeao(peca:PecaXadrez, tabuleiro_movimentos:list):
    if verificarSePeaoPodeAvancarUmaCasa(peca, tabuleiro_movimentos) == True:
        verificarSePeaoPodeAvancarDuasCasas(peca, tabuleiro_movimentos)

    for c in range(2):
        # representa os movimentos para tomar peças inimigas na diagonal. na segunda execução, troca para a segunda diagonal
        possivel_ocupacao_linha = peca.indice_linha_atual + peca.tipos_movimentos[2+c][0]
        possivel_ocupacao_coluna = peca.indice_coluna_atual + peca.tipos_movimentos[2+c][1]
        possivel_ocupacao = [possivel_ocupacao_linha, possivel_ocupacao_coluna]

        if verificarSePeaoPodeAvançarEmDiagonal(possivel_ocupacao) == True:
            verificarSePeaoPodeCapturarEmDiagonal(possivel_ocupacao, tabuleiro_movimentos)
        verificarSePeaoPodeCapturarEnPassant(peca, c, possivel_ocupacao, tabuleiro_movimentos)

def testarSePossivelOcupacaoEhValida(possivel_ocupacao:Cordenadas):
    if str(possivel_ocupacao.indice_linha) in settings.indices_tabuleiro and str(possivel_ocupacao.indice_coluna) in settings.indices_tabuleiro:
        return True
    return False

def verificarSePeaoPodeCapturarEnPassant(peca:PecaXadrez, c:int, possivel_ocupacao:list, tabuleiro_movimentos:list):
    if peca.passant_direita == True and c == 1 or peca.passant_esquerda == True and c == 0:
        tabuleiro_movimentos[possivel_ocupacao[0]][possivel_ocupacao[1]] = settings.movimento_possivel
        settings.tabuleiro_principal[possivel_ocupacao[0]][possivel_ocupacao[1]] = settings.movimento_possivel

def verificarSePeaoPodeCapturarEmDiagonal(possivel_ocupacao:list, tabuleiro_movimentos:list):
    peca_na_possivel_ocupacao = pecas.descobrirPeca(possivel_ocupacao[0], possivel_ocupacao[1])
    if settings.jogador_atual == Jogador.JOGADOR_DE_BRANCAS and peca_na_possivel_ocupacao.aparencia in settings.pecas_jogador_de_pretas and settings.tabuleiro_principal[possivel_ocupacao[0]][possivel_ocupacao[1]].aparencia != "":
        tabuleiro_movimentos[possivel_ocupacao[0]][possivel_ocupacao[1]] = settings.movimento_possivel
    elif settings.jogador_atual == Jogador.JOGADOR_DE_PRETAS and peca_na_possivel_ocupacao.aparencia in settings.pecas_jogador_de_brancas and settings.tabuleiro_principal[possivel_ocupacao[0]][possivel_ocupacao[1]].aparencia != "":
        tabuleiro_movimentos[possivel_ocupacao[0]][possivel_ocupacao[1]] = settings.movimento_possivel

def verificarSePeaoPodeAvançarEmDiagonal(possivel_ocupacao:list):
    if str(possivel_ocupacao[0]) in settings.indices_tabuleiro and str(possivel_ocupacao[1]) in settings.indices_tabuleiro:
        return True
    return False

def verificarSePeaoPodeAvancarUmaCasa(peca:PecaXadrez, tabuleiro_movimentos:list):
    # representa o movimento do peão para 1 casa em sua frente
    possivel_ocupacao_linha = peca.indice_linha_atual + peca.tipos_movimentos[0][0] 
    possivel_ocupacao_coluna = peca.indice_coluna_atual + peca.tipos_movimentos[0][1]

    if str(possivel_ocupacao_linha) in settings.indices_tabuleiro and settings.tabuleiro_principal[possivel_ocupacao_linha][peca.indice_coluna_atual].classe == "vazio":
        settings.tabuleiro_principal[possivel_ocupacao_linha][possivel_ocupacao_coluna] = settings.movimento_possivel
        tabuleiro_movimentos[possivel_ocupacao_linha][possivel_ocupacao_coluna] = settings.movimento_possivel
        return True
    return False

def verificarSePeaoPodeAvancarDuasCasas(peca:PecaXadrez, tabuleiro_movimentos:list):
    # representa o movimento do peão para 2 casas em sua frente
    possivel_ocupacao_linha = peca.indice_linha_atual + peca.tipos_movimentos[1][0]
    possivel_ocupacao_coluna = peca.indice_coluna_atual + peca.tipos_movimentos[1][1]

    posicao_inicial_peao = ["1", "6"]
    if str(possivel_ocupacao_linha) in settings.indices_tabuleiro and str(peca.indice_linha_atual) in posicao_inicial_peao and settings.tabuleiro_principal[possivel_ocupacao_linha][peca.indice_coluna_atual].classe == "vazio":
        settings.tabuleiro_principal[possivel_ocupacao_linha][possivel_ocupacao_coluna] = settings.movimento_possivel
        tabuleiro_movimentos[possivel_ocupacao_linha][possivel_ocupacao_coluna] = settings.movimento_possivel

def verificarSeRoqueEhUmaOpcaoValida(peca:PecaXadrez, movimento:list, tabuleiro_movimentos:list):
    roque_foi_encontrado = False
    # Testa se o movimento sendo avaliado é o roque do rei (longo ou curto)
    if peca.classe == "rei" and movimento == peca.tipos_movimentos[8] or peca.classe == "rei" and movimento == peca.tipos_movimentos[9]:
        # Separa a lógica de teste entre roque curto (primeiro) e roque longo (segundo)
        potencial_torre = pecas.descobrirPeca(peca.indice_linha_atual, 7)
        if peca.classe == "rei" and movimento == peca.tipos_movimentos[8] and potencial_torre.classe == "torre":
            # testa se as condições para o roque são válidas (rei e torre não terem se movido e espaço livre entre as peças)
            if peca.se_moveu == False and potencial_torre.se_moveu == False and potencial_torre.time == peca.time and pecas.descobrirPeca(peca.indice_linha_atual, 6).classe == "vazio" and pecas.descobrirPeca(peca.indice_linha_atual, 5).classe == "vazio":
                # se o roque for válido, adiciona essa opção de movimento para o usuário
                settings.tabuleiro_principal[peca.indice_linha_atual][peca.indice_coluna_atual+2] = settings.movimento_possivel
                tabuleiro_movimentos[peca.indice_linha_atual][peca.indice_coluna_atual+2] = settings.movimento_possivel
                roque_foi_encontrado = True
        potencial_torre = pecas.descobrirPeca(peca.indice_linha_atual, 0)
        if peca.classe == "rei" and movimento == peca.tipos_movimentos[9] and potencial_torre.classe == "torre":
            if peca.se_moveu == False and potencial_torre.se_moveu == False and potencial_torre.time == peca.time and pecas.descobrirPeca(peca.indice_linha_atual, 1).classe == "vazio" and pecas.descobrirPeca(peca.indice_linha_atual, 2).aparencia == "vazio" and pecas.descobrirPeca(peca.indice_linha_atual, 3).aparencia == "vazio":
                settings.tabuleiro_principal[peca.indice_linha_atual][peca.indice_coluna_atual-2] = settings.movimento_possivel
                tabuleiro_movimentos[peca.indice_linha_atual][peca.indice_coluna_atual+2] = settings.movimento_possivel
                roque_foi_encontrado = True
    return roque_foi_encontrado

def verificarSeNovaPosicaoEstaLivre(possivel_ocupacao:Cordenadas, tabuleiro_movimentos:list):
    if pecas.descobrirPeca(possivel_ocupacao.indice_linha, possivel_ocupacao.indice_coluna).classe == "vazio":
        settings.tabuleiro_principal[possivel_ocupacao.indice_linha][possivel_ocupacao.indice_coluna] = settings.movimento_possivel
        tabuleiro_movimentos[possivel_ocupacao.indice_linha][possivel_ocupacao.indice_coluna] = settings.movimento_possivel

def verificarSeNovaPosicaoEstaOcupadaPeloTimeInimigo(possivel_ocupacao:Cordenadas, tabuleiro_movimentos:list):
    posicao_analizada = pecas.descobrirPeca(possivel_ocupacao.indice_linha, possivel_ocupacao.indice_coluna)
    # TODO: depois checar se 'posicao_analizada.aparencia != ""' é realmente necessário
    if posicao_analizada.aparencia in settings.pecas_jogador_de_pretas and posicao_analizada.aparencia != "" and settings.jogador_atual == Jogador.JOGADOR_DE_BRANCAS.value or posicao_analizada.aparencia in settings.pecas_jogador_de_brancas and posicao_analizada.aparencia != "" and settings.jogador_atual == Jogador.JOGADOR_DE_PRETAS.value:
        tabuleiro_movimentos[possivel_ocupacao.indice_linha][possivel_ocupacao.indice_coluna] = settings.movimento_possivel
        return True
    return False


def executarMovimento(peca:PecaXadrez, nova_cordenada:list):
    # TODO: uma função deve ser adicionada para atualizar a posição de uma peça após seu movimento
    executarAcoesEspecificasMovimentoEnPassant(peca, nova_cordenada)
    tabuleiros.limparPassantsPossiveis(settings.tabuleiro_principal)
    executarAcoesEspecificasMovimentoPermitaNovoEnPassant(peca, nova_cordenada)
    executarAcoesEspecificasMovimentoPromocaoPeao(peca, nova_cordenada)
    executarAcoesEspecificasMovimentoRoque(peca, nova_cordenada)

    executarAcoesGeraisParaQualquerMovimento(peca, nova_cordenada)

def executarAcoesEspecificasMovimentoEnPassant(peca:PecaXadrez, nova_cordenada:list):
    if peca.classe == "peao" and settings.tabuleiro_principal[nova_cordenada[0]][nova_cordenada[1]].aparencia == "•" and nova_cordenada[1] != peca.indice_coluna_atual:
        if settings.jogador_atual == Jogador.JOGADOR_DE_BRANCAS:
            settings.tabuleiro_principal[nova_cordenada[0]+1][nova_cordenada[1]] = settings.espaco_vazio
        else:
            settings.tabuleiro_principal[nova_cordenada[0]-1][nova_cordenada[1]] = settings.espaco_vazio

def executarAcoesEspecificasMovimentoPermitaNovoEnPassant(peca:PecaXadrez, nova_cordenada:list):
    if nova_cordenada[0] - peca.indice_linha_atual == 2 and peca.aparencia == "♙" or nova_cordenada[0] - peca.indice_linha_atual == -2 and peca.aparencia == "♟":
        if nova_cordenada[0] - peca.indice_linha_atual == 2 and nova_cordenada[1]-1 >= 0:
            if pecas.descobrirPeca(nova_cordenada[0], nova_cordenada[1]-1).aparencia == "♟":
                pecas.descobrirPeca(nova_cordenada[0], nova_cordenada[1]-1).passant_direita = True
        if nova_cordenada[0] - peca.indice_linha_atual == 2 and nova_cordenada[1]+1 < 8:
            if pecas.descobrirPeca(nova_cordenada[0], nova_cordenada[1]+1).aparencia == "♟":
                pecas.descobrirPeca(nova_cordenada[0], nova_cordenada[1]+1).passant_esquerda = True
        if nova_cordenada[0] - peca.indice_linha_atual == -2 and nova_cordenada[1]-1 >= 0:
            if pecas.descobrirPeca(nova_cordenada[0], nova_cordenada[1]-1).aparencia == "♙":
                pecas.descobrirPeca(nova_cordenada[0], nova_cordenada[1]-1).passant_direita = True
        if nova_cordenada[0] - peca.indice_linha_atual == -2 and nova_cordenada[1]+1 < 8:
            if pecas.descobrirPeca(nova_cordenada[0], nova_cordenada[1]+1).aparencia == "♙":
                pecas.descobrirPeca(nova_cordenada[0], nova_cordenada[1]+1).passant_esquerda = True

def executarAcoesEspecificasMovimentoPromocaoPeao(peca:PecaXadrez, nova_cordenada:list):
    if peca.aparencia == "♙" and nova_cordenada[0] == 7 or peca.aparencia == "♟" and nova_cordenada[0] == 0:
        peca.promovido = True

def executarAcoesEspecificasMovimentoRoque(peca:PecaXadrez, nova_cordenada:list):
    if nova_cordenada[1] - peca.indice_coluna_atual == 2 and peca.classe == "rei" and peca.se_moveu == False or nova_cordenada[1] - peca.indice_coluna_atual == -2 and peca.classe in "rei" and peca.se_moveu == False:
        if nova_cordenada[1] < 4:
            settings.tabuleiro_principal[nova_cordenada[0]][nova_cordenada[1]+1] = settings.tabuleiro_principal[nova_cordenada[0]][nova_cordenada[1]-2]
            settings.tabuleiro_principal[nova_cordenada[0]][nova_cordenada[1]-2] = settings.espaco_vazio
        else:
            settings.tabuleiro_principal[nova_cordenada[0]][nova_cordenada[1]-1] = settings.tabuleiro_principal[nova_cordenada[0]][nova_cordenada[1]+1]
            settings.tabuleiro_principal[nova_cordenada[0]][nova_cordenada[1]+1] = settings.espaco_vazio

def executarAcoesGeraisParaQualquerMovimento(peca:PecaXadrez, nova_cordenada:list):
    peca.se_moveu = True
    settings.tabuleiro_principal[nova_cordenada[0]][nova_cordenada[1]] = peca
    settings.tabuleiro_principal[peca.indice_linha_atual][peca.indice_coluna_atual] = settings.espaco_vazio