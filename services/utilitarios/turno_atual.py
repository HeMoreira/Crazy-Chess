from settings import settings
from services.tabuleiro import cheques, tabuleiros, posicoes, movimentos, pecas
from services.utilitarios import fim_de_jogo
import copy

def turnoAtual(jogador):
    # global settings.jogador_atual, settings.partida_rolando, settings.tabuleiro_principal
    if jogador == True:
        print("\n\n\n\n- VEZ DAS BRANCAS ♚\n")
    else:
        print("\n\n\n\n- VEZ DAS PRETAS ♔\n")
    while True:
        if cheques.testarChequeMate() == "MATE":
            print("=====================================================") 
            print("                 -= ! CHEQUE MATE ! =-               ")
            print("  Seu rei foi encurralado, esse é o fim para você..  ")
            print("=====================================================")
            tabuleiros.imprimirTabuleiro(jogador)
            settings.partida_rolando = False
            fim_de_jogo.fimDeJogo("cheque-mate")
            return
        elif cheques.testarChequeMate() == "AFOGAMENTO":
            print("=====================================================") 
            print("                 -= ! AFOGAMENTO ! =-                ")
            print("  Você não é capaz de passar a vez, empate forçado!  ")
            print("=====================================================")
            tabuleiros.imprimirTabuleiro(jogador)
            settings.partida_rolando = False
            fim_de_jogo.fimDeJogo("afogamento")
            return
        elif cheques.testarCheque() == True:
            print("=====================================================") 
            print("                   -= ! CHEQUE ! =-                  ")
            print("  Seu rei está sob ameaça, defenda-o imediatamente!  ")
            print("=====================================================") 
        
        peca_escolhida = "aaaaaa"
        nova_posicao = "aaaaaaaa"
        se_peca_selecionada = False
        posicao1 = 0
        posicao2 = 0
        peca = None
        abortar = True
        while abortar == True:
            abortar = False
            while se_peca_selecionada == False:
                tabuleiros.imprimirTabuleiro(jogador)
                entrada_valida = False
                while entrada_valida == False:
                    print("==========================================================================================================") 
                    peca_escolhida = input("Digite as cordenadas da peça desejada (ex: b2 para selecionar ou b2b4 para selecionar e mover):\nVocê também pode desistir (desistir) ou pedir por empate (empate) se quiser\nResposta: ")
                    if peca_escolhida.lower() == "desistir":
                        settings.partida_rolando = False
                        fim_de_jogo.fimDeJogo("desistencia")
                        return
                    if peca_escolhida.lower() == "empate":
                        resposta = fim_de_jogo.tentativaEmpate()
                        if resposta == "sim":
                            settings.partida_rolando = False
                            fim_de_jogo.fimDeJogo("empate")
                            return
                        elif resposta == "nao" or resposta == "não":
                            print("=====================================================") 
                            print("            O pedido de EMPATE foi NEGADO!           ")
                            print("   Alguém está confiante.. e a partida continua!!    ")
                            print("=====================================================")
                            continue
                    elif len(peca_escolhida) == 2:
                        if posicoes.testarValidezCoordenada(peca_escolhida, False, settings.tabuleiro_principal) == 0:
                            entrada_valida = True
                        else:
                            posicoes.imprimirValidezCoordenada(peca_escolhida, False, settings.tabuleiro_principal)
                            continue
                        se_peca_selecionada = True
                        posicao1, posicao2 = posicoes.descobrirPosicao(peca_escolhida)
                        peca = pecas.descobrirPeca(posicao1, posicao2)
                        tabuleiro_movimentos = movimentos.mostrarMovimentosValidos(peca, posicao1, posicao2, settings.jogador_atual)
                        tabuleiros.imprimirTabuleiro(jogador)
                    elif len(peca_escolhida) == 4:
                        nova_posicao = peca_escolhida[2]+peca_escolhida[3]
                        peca_escolhida = peca_escolhida[0]+peca_escolhida[1]
                        if posicoes.testarValidezCoordenada(peca_escolhida[0]+peca_escolhida[1], False, settings.tabuleiro_principal) == 0:
                            entrada_valida = True
                        else:
                            entrada_valida = False
                            peca_escolhida = "aaaaaa"
                            nova_posicao = "aaaaaaaa"
                            se_peca_selecionada = False
                            continue
                        se_peca_selecionada = True
                        posicao1, posicao2 = posicoes.descobrirPosicao(peca_escolhida)
                        peca = pecas.descobrirPeca(posicao1, posicao2)
                        tabuleiro_movimentos = movimentos.mostrarMovimentosValidos(peca, posicao1, posicao2, settings.jogador_atual)
                        tabuleiros.imprimirTabuleiro(jogador)
                        if posicoes.testarValidezCoordenada(nova_posicao, True, tabuleiro_movimentos) != 0:
                            entrada_valida = False
                            peca_escolhida = "aaaaaa"
                            nova_posicao = "aaaaaaaa"
                            se_peca_selecionada = False
                            movimentos.limparMovimentosPossiveis(settings.tabuleiro_principal)
                            tabuleiros.imprimirTabuleiro(settings.jogador_atual)
                            continue
                        posicoes.imprimirValidezCoordenada(peca_escolhida, False, settings.tabuleiro_principal)
                        posicoes.imprimirValidezCoordenada(nova_posicao, True, tabuleiro_movimentos)
                while posicoes.testarValidezCoordenada(nova_posicao, True, tabuleiro_movimentos) != 0 and se_peca_selecionada == True:
                    print("==========================================================================================================") 
                    nova_posicao = input("Para onde essa peça deve ir? (ex: b4)\nVocê também pode trocar de peça (trocar)\nResposta: ")
                    if nova_posicao.lower() == "trocar":
                        se_peca_selecionada = False
                        peca_escolhida = "aaaaaaba"
                        print("trocando a peça...")
                        movimentos.limparMovimentosPossiveis(settings.tabuleiro_principal)
                        break
                    posicoes.imprimirValidezCoordenada(nova_posicao, True, tabuleiro_movimentos)
            tabuleiro_suporte = copy.deepcopy(settings.tabuleiro_principal)
            movimentos.limparMovimentosPossiveis(tabuleiro_suporte)
            nova_posicao1, nova_posicao2 = posicoes.descobrirPosicao(nova_posicao)
            movimentos.executarMovimento(peca, posicao1, posicao2, nova_posicao1, nova_posicao2)
            if cheques.testarCheque() == False:
                movimentos.limparMovimentosPossiveis(settings.tabuleiro_principal)
            else:
                settings.tabuleiro_principal = copy.deepcopy(tabuleiro_suporte)
                movimentos.limparMovimentosPossiveis(settings.tabuleiro_principal)
                print("Você não pode deixar seu rei ser derrotado.. Faça outro movimento!")
                abortar = True
                settings.tabuleiro_principal = copy.deepcopy(tabuleiro_suporte)
                se_peca_selecionada = False
                peca_escolhida = "aaaaaaba"
                nova_posicao = "bbbbbbbbab"
                continue
            if peca.aparencia in "♙♟":
                if peca.promovido == True:
                    pecas.PromoverPeao(peca, nova_posicao1, nova_posicao2)
            tabuleiros.imprimirTabuleiro(jogador)
            confirmacao = "aaaaa"
            while confirmacao.lower() != "" and confirmacao.lower() != "cancelar":
                confirmacao = input("Confirme o movimento pressione enter ou retroceda digitando 'cancelar': ")
            if confirmacao.lower() == "cancelar":
                abortar = True
                settings.tabuleiro_principal = copy.deepcopy(tabuleiro_suporte)
                se_peca_selecionada = False
                peca_escolhida = "aaaaaaba"
                nova_posicao = "bbbbbbbbab"
                print("Refazendo movimento...")
                movimentos.limparMovimentosPossiveis(settings.tabuleiro_principal)
        break
    if jogador == True:
        settings.jogador_atual = False
    else:
        settings.jogador_atual = True
    if settings.partida_rolando == True:
        turnoAtual(settings.jogador_atual)
    else:
        print("A partida acabou...")
        return