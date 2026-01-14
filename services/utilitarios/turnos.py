from settings import settings
from models.enums_utilitarios import StatusDePartida, TipoDeEntradaInicial
from models.cords import Cordenadas
from services.tabuleiro import cheques, posicoes, tabuleiros, pecas, movimentos
from services.utilitarios import impressoes, fim_de_jogo
import copy


def executarTurnoAtual():
    impressoes.imprimirDeQuemEhAVezDeJogar()
    tabuleiros.imprimirTabuleiro()
    status_da_partida = checarStatusDaPartidaParaTurnoAtual()
    if status_da_partida == StatusDePartida.CHEQUE_MATE or status_da_partida == StatusDePartida.AFOGAMENTO:
        return
    entrada_inicial_do_jogador, tipo_de_entrada = obterSelecaoDePecaDoJogadorAtual()
    responderACadaTipoDeEntradaInicialDoJogador(entrada_inicial_do_jogador, tipo_de_entrada)
    if settings.rodada_finalizada_com_sucesso == True:
        return
    else:
        executarTurnoAtual()

def checarStatusDaPartidaParaTurnoAtual():
    match cheques.testarSeFimDeJogoParaJogadorAtual():
        case StatusDePartida.CHEQUE_MATE:
            fim_de_jogo.fimDeJogo(StatusDePartida.CHEQUE_MATE)
            return StatusDePartida.CHEQUE_MATE
        case StatusDePartida.AFOGAMENTO:
            fim_de_jogo.fimDeJogo(StatusDePartida.AFOGAMENTO)
            return StatusDePartida.AFOGAMENTO
        case StatusDePartida.CHEQUE:
            impressoes.imprimirCabecalhoComSubtitulo("! CHEQUE !", "Seu rei está sob ameaça, defenda-o imediatamente!")
            return StatusDePartida.CHEQUE
        case _:
            return StatusDePartida.NORMAL

def obterSelecaoDePecaDoJogadorAtual():
    while True:
        impressoes.imprimirDivisoria()
        entrada_de_selecao_de_peca = input("Digite as cordenadas da peça desejada.\nEx: 'b2' para selecionar ou 'b2b4' para selecionar e mover.\nVocê também pode 'desistir' ou pedir por 'empate'.\nResposta: ")
        entrada_formatada = entrada_de_selecao_de_peca.lower().strip()
        if entrada_formatada == "desistir":
            return [], TipoDeEntradaInicial.DESISTENCIA
        elif entrada_formatada == "empate":
            return [], TipoDeEntradaInicial.EMPATE
        elif len(entrada_formatada) == 2:
            cordenadas = posicoes.converterEntradaEmCordenada(entrada_formatada)
            if posicoes.testarValidezCordenadasDaPeca(cordenadas) == True:
                return [cordenadas], TipoDeEntradaInicial.SELECAO_DE_PECA
        elif len(entrada_formatada) == 4:
            cordenadas = posicoes.converterEntradaEmCordenada(entrada_formatada[0:2])
            novas_cordenadas = posicoes.converterEntradaEmCordenada(entrada_formatada[2:4])
            if posicoes.testarValidezCordenadasDaPeca(cordenadas) == True and posicoes.testarValidezCordenadasDaNovaPosicao(cordenadas, novas_cordenadas) == True:
                return [cordenadas, novas_cordenadas], TipoDeEntradaInicial.SELECAO_E_MOVIMENTO_DE_PECA
        else:
            print("Digite as cordenadas corretamente...")

def obterNovaPosicaoDaPecaDoJogadorAtual(cordenadas:Cordenadas):
    while True:
        tabuleiros.imprimirTabuleiro()
        impressoes.imprimirDivisoria()
        nova_posicao = input("Para onde essa peça deve ir? (ex: b4)\nVocê também pode 'trocar' de peça\nResposta: ")
        nova_posicao_formatada = nova_posicao.lower().strip()
        if nova_posicao_formatada == "trocar":
            print("trocando a peça...")
            settings.rodada_finalizada_com_sucesso = False
            return None
        elif len(nova_posicao_formatada) == 2:
            nova_posicao_convertida = posicoes.converterEntradaEmCordenada(nova_posicao_formatada)
            if posicoes.testarValidezCordenadasDaNovaPosicao(cordenadas, nova_posicao_convertida) == True:
                return nova_posicao_convertida
        else:
            print("Digite as cordenadas corretamente...")

def responderACadaTipoDeEntradaInicialDoJogador(entrada_do_jogador:list[Cordenadas], tipo_de_entrada:TipoDeEntradaInicial):
    match tipo_de_entrada:
        case TipoDeEntradaInicial.DESISTENCIA:
            responderADesistenciaDoJogadorAtual()
        case TipoDeEntradaInicial.EMPATE:
            responderAPedidoDeEmpateDoJogadorAtual()
        case TipoDeEntradaInicial.SELECAO_DE_PECA:
            responderASelecaoDePecaDoJogadorAtual(entrada_do_jogador)
        case TipoDeEntradaInicial.SELECAO_E_MOVIMENTO_DE_PECA:
            responderAMovimentacaoDePecaDoJogadorAtual(entrada_do_jogador)

def responderADesistenciaDoJogadorAtual():
    settings.rodada_finalizada_com_sucesso = True
    fim_de_jogo.fimDeJogo(StatusDePartida.DESISTENCIA)

def responderAPedidoDeEmpateDoJogadorAtual():
    if fim_de_jogo.tentarPedidoPorEmpate() == True:
        settings.rodada_finalizada_com_sucesso = True
        fim_de_jogo.fimDeJogo(StatusDePartida.EMPATE_ACEITO)
    else:
        impressoes.imprimirCabecalhoComSubtitulo("O pedido de EMPATE foi NEGADO!", "Alguém está confiante... E a partida continua!!")

def responderASelecaoDePecaDoJogadorAtual(entrada_do_jogador:list[Cordenadas]):
    cordenadas = entrada_do_jogador[0]
    peca = pecas.descobrirPeca(cordenadas)
    lista_de_movimentos = movimentos.descobrirMovimentosValidos(peca)
    tabuleiros.exibirMovimentosPossiveis(lista_de_movimentos)
    tabuleiros.imprimirTabuleiro()
    novas_cordenadas = obterNovaPosicaoDaPecaDoJogadorAtual(cordenadas)
    if novas_cordenadas == None:
        return
    if posicoes.testarValidezCordenadasDaNovaPosicao(cordenadas, novas_cordenadas) == True:
        nova_lista_de_cordenadas = entrada_do_jogador
        nova_lista_de_cordenadas.append(novas_cordenadas)
        responderAMovimentacaoDePecaDoJogadorAtual(nova_lista_de_cordenadas)

def responderAMovimentacaoDePecaDoJogadorAtual(entrada_do_jogador:list[Cordenadas]):
    cordenadas = entrada_do_jogador[0]
    novas_cordenadas = entrada_do_jogador[1]
    peca = pecas.descobrirPeca(cordenadas)
    tabuleiros.imprimirTabuleiro()

    tabuleiro_suporte = copy.deepcopy(settings.tabuleiro_principal)
    movimentos.executarMovimento(peca, novas_cordenadas)
    tabuleiros.limparMovimentosPossiveis()

    if movimentos.testarSeMovimentoResultaEmCheque() == True:
        desfazerMovimento(tabuleiro_suporte)
        return
    pecas.promoverPeaoSeEmCasaDePromocao(peca)
    tabuleiros.imprimirTabuleiro()
    if confirmarJogada(tabuleiro_suporte) == False:
        desfazerMovimento(tabuleiro_suporte)
        return

def desfazerMovimento(tabuleiro_suporte:list):
    settings.tabuleiro_principal = copy.deepcopy(tabuleiro_suporte)
    settings.rodada_finalizada_com_sucesso = False
    movimentos.limparMovimentosPossiveis()

def confirmarJogada(tabuleiro_suporte:list):
    if pedirConfirmacaoDaJogada() == True:
        settings.rodada_finalizada_com_sucesso = True
        return True
    else:
        print("Refazendo movimento...")
        settings.tabuleiro_principal = copy.deepcopy(tabuleiro_suporte)
        settings.rodada_finalizada_com_sucesso = False
        movimentos.limparMovimentosPossiveis()
        return False
    
def pedirConfirmacaoDaJogada():
    confirmacao = "Entrada Inválida"
    while confirmacao.lower() != "" and confirmacao.lower() != "cancelar":
        confirmacao = input("Confirme o movimento pressionando enter.\nRetroceda digitando 'cancelar'\nResposta: ")
    if confirmacao.lower() == "cancelar":
        print("Refazendo movimento...")
        movimentos.limparMovimentosPossiveis()
        return False
    return True