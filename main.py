tabuleiro_base = [["♖","♘","♗","♕","♔","♗","♘","♖"],["♙","♙","♙","♙","♙","♙","♙","♙"],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],["♟","♟","♟","♟","♟","♟","♟","♟"],["♜","♞","♝","♛","♚","♝","♞","♜"]] 
tabuleiro_principal = [["♖","♘","♗","♕","♔","♗","♘","♖"],["♙","♙","♙","♙","♙","♙","♙","♙"],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],["♟","♟","♟","♟","♟","♟","♟","♟"],["♜","♞","♝","♛","♚","♝","♞","♜"]] 
#tabuleiro_principal = [["♖","♘","♗","♕","♔","♗","♘","♖"],["♙","♙"," ","♙"," ","♙","♙"," "],[" ","♙"," "," "," "," "," "," "],[" "," ","♙"," "," "," "," "," "],[" "," "," ","♟"," "," "," "," "],[" "," "," "," "," "," "," "," "],["♟","♟"," "," ","♟","♟","♟"," "],["♜","♞","♝","♛","♚","♝","♞","♜"]] 
numeros_tabuleiro = ["8","7","6","5","4","3","2","1"]
conversao_coluna = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}

class pecaXadrez:
    aparencia = ""
    tipos_movimentos = []
    time = True
    tipo_de_movimento = ""
    #| UNICO | INFINITO | PEAO |
    def __init__(self, tipos_movimentos:list, time:bool, aparencia:str, tipo_de_movimento:str):
        self.aparencia = aparencia
        self.tipos_movimentos = tipos_movimentos
        self.time = time
        self.tipo_de_movimento = tipo_de_movimento

bispo_preto = pecaXadrez([[-1, -1], [-1, 1], [1, -1], [1, 1]], False, "♗", "INFINITO")
bispo_branco = pecaXadrez([[-1, -1], [-1, 1], [1, -1], [1, 1]], True, "♝", "INFINITO")
torre_preto = pecaXadrez([[-1, 0], [1, 0], [0, -1], [0, 1]], False, "♖", "INFINITO")
torre_branco = pecaXadrez([[-1, 0], [1, 0], [0, -1], [0, 1]], True, "♜", "INFINITO")
cavalo_preto = pecaXadrez([[2, -1], [2, 1], [-2, -1], [-2, 1], [-1, 2], [1, 2], [-1, -2], [1, -2]], False, "♘", "UNICO")
cavalo_branco = pecaXadrez([[2, -1], [2, 1], [-2, -1], [-2, 1], [-1, 2], [1, 2], [-1, -2], [1, -2]], True, "♞", "UNICO")
rainha_preto = pecaXadrez([[-1, -1], [-1, 1], [1, -1], [1, 1], [-1, 0], [1, 0], [0, -1], [0, 1]], False, "♕", "INFINITO")
rainha_branco = pecaXadrez([[-1, -1], [-1, 1], [1, -1], [1, 1], [-1, 0], [1, 0], [0, -1], [0, 1]], True, "♛", "INFINITO")
rei_preto = pecaXadrez([[-1, -1], [-1, 1], [1, -1], [1, 1], [-1, 0], [1, 0], [0, -1], [0, 1]], False, "♔", "UNICO")
rei_branco = pecaXadrez([[-1, -1], [-1, 1], [1, -1], [1, 1], [-1, 0], [1, 0], [0, -1], [0, 1]], True, "♚", "UNICO")
peao_preto = pecaXadrez([[1, 0], [2, 0], [1, -1], [1, 1]], False, "♙", "PEAO")
peao_branco = pecaXadrez([[-1, 0], [-2, 0], [-1, -1], [-1, 1]], True, "♟", "PEAO")

#Criando Objetos das peças do tabuleiro
lista_pecas = [bispo_preto, bispo_branco, torre_preto, torre_branco, cavalo_preto, cavalo_branco, rainha_preto, rainha_branco, rei_preto, rei_branco, peao_preto, peao_branco]
 
#BRANCAS = TRUE, PRETAS = FALSE
partida_rolando = True
jogador_atual = True
pos_passant1 = 0
pos_passant2 = 0

def imprimirTabuleiro(jogador): 
    impressao = ""
    tabuleiro_suporte = tabuleiro_principal.copy()
    numeros_tabuleiro_suporte = numeros_tabuleiro
    """
    if jogador == False:
        ajudante = 7
        numeros_tabuleiro_suporte = ["","","","","","","",""] 
        for linha in range(len(tabuleiro_suporte)):
            tabuleiro_suporte[linha] = tabuleiro_principal[ajudante]
            numeros_tabuleiro_suporte[linha] = numeros_tabuleiro[ajudante]
            ajudante-=1
    """
        
    print("   _______________________") 
    linha_atual = 0 
    impressao = impressao + f"{numeros_tabuleiro_suporte[linha_atual]}" 
    linha_atual+=1 
    for linha in range(len(tabuleiro_suporte)):
        for coluna in range(8):
            impressao = impressao + " |" + tabuleiro_suporte[linha][coluna] 
            if (coluna+1) % 8 == 0 and linha+1 != 8:
                impressao = impressao + " |\n" 
                impressao = impressao + f"{numeros_tabuleiro_suporte[linha_atual]}" 
                linha_atual+=1 
            elif (coluna+1) % 8 == 0:
                impressao = impressao + " |" 
    print(impressao) 
    print("   ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯") 
    print("    a  b  c  d  e  f  g  h") 

def descobrirPosicao(coordenadas):
    cord_y = 1000
    for chave, valor in conversao_coluna.items():
        if chave == coordenadas[0]:
            cord_y = valor
    if cord_y == 1000:
        return -1, -1
    cord_x = 100
    if coordenadas[1] in "12345678":
        cord_x = int(coordenadas[1])
    else:
        return -1, -1
    pos1 = 8-(cord_x)
    pos2 = cord_y-1
    return pos1, pos2

def introducaoPartida():
    print("Que começem os Jogos..") 
    print("=====================================================") 
    print("-= PARTIDA DE XADREZ PERSONALIZADA: PARTIDA NORMAL =-") 
    print("=====================================================") 
    print("\n")
    global partida_rolando, jogador_atual
    partida_rolando = True
    jogador_atual = True
    global pos_passant1, pos_passant2
    pos_passant1 = 0
    pos_passant2 = 0
    turnoAtual(jogador_atual)

def descobrirPeca(posicao1, posicao2):
    return tabuleiro_principal[posicao1][posicao2]

def testarValidezPeca(peca, se_nova_posicao):
    if peca == " " and se_nova_posicao == False:
        return 3
    elif peca in "♔♕♖♗♘♙" and peca != "" and jogador_atual == True and se_nova_posicao == False:
        return 4
    elif peca in "♚♛♜♝♞♟" and peca != "" and jogador_atual == False and se_nova_posicao == False:
        return 4
    elif se_nova_posicao == True and peca != "•":
        return 5
    else:
        return 0

def testarValidezCoordenada(entrada, se_nova_posicao, tabuleiro):
    #print(entrada, se_nova_posicao, tabuleiro)
    posicao1, posicao2 = descobrirPosicao(entrada)
    if posicao1 == -1:
        return 2
    else:
        peca = ""
        peca = tabuleiro[posicao1][posicao2]
        return testarValidezPeca(peca, se_nova_posicao)
    """
    elif len(entrada) == 4:
        cordenada1 = entrada[0]+entrada[1]
        cordenada2 = entrada[2]+entrada[3]
        cord1_posicao1, cord1_posicao2 = descobrirPosicao(cordenada1)
        cord2_posicao1, cord2_posicao2 = descobrirPosicao(cordenada2)
        if cord1_posicao1 == -1 or cord2_posicao1 == -1:
            return 2
        else:
            peca = ""
            peca = tabuleiro[cord1_posicao1][cord1_posicao2]
            teste1 = testarValidezPeca(peca, se_nova_posicao)
            tabuleiro_movimentos = mostrarMovimentosValidos(peca, cord1_posicao1, cord1_posicao2)
            #imprimirTabuleiro(jogador_atual)
            nova_posicao = ""
            nova_posicao = tabuleiro_movimentos[cord2_posicao1][cord2_posicao2]
            teste2 = testarValidezPeca(nova_posicao, True)
            #print(teste1, teste2)
            if teste1 == 0 and teste2 == 0:
                return 0
            else:
                return 6
            #limparMovimentosPossiveis(tabuleiro_principal)
        """

def imprimirValidezCoordenada(entrada, se_nova_posicao, tabuleiro):
    if testarValidezCoordenada(entrada, se_nova_posicao, tabuleiro) != 0:
        if testarValidezCoordenada(entrada, se_nova_posicao, tabuleiro) == 1:
            print("Coordenada Inválida, as coordenadas só podem ter 2 ou 4 caractéres..")
        elif testarValidezCoordenada(entrada, se_nova_posicao, tabuleiro) == 2:
            print("Coordenada Inválida, digite as coordenadas no formato de [coluna][linha]..")
        elif testarValidezCoordenada(entrada, se_nova_posicao, tabuleiro) == 3:
            print("Coordenada Inválida, Não tem nenhuma peça nessa posição..")
        elif testarValidezCoordenada(entrada, se_nova_posicao, tabuleiro) == 4:
            print("Coordenada Inválida, você não pode mover esta peça..")
        elif testarValidezCoordenada(entrada, se_nova_posicao, tabuleiro) == 5:
            print("Coordenada Inválida, esta peça não pode ir para esta posição..")
        elif testarValidezCoordenada(entrada, se_nova_posicao, tabuleiro) == 6:
            print("Coordenada Inválida, alguma das informações digitadas não foi aceita..")
        return 0
    else:
        return 1

def novoTabuleiroVazio():
    tabuleiro = [[],[],[],[],[],[],[],[]]
    for i in range(8):
        tabuleiro[i] = [" "]*8
    return tabuleiro

def descobrirMovimentosValidos(peca, posicao1, posicao2):
    tabuleiro_movimentos = novoTabuleiroVazio()
    if lista_pecas[peca].tipo_de_movimento == "PEAO":

        teste_movimento = posicao1 + lista_pecas[peca].tipos_movimentos[0][0]
        if str(teste_movimento) in "01234567" and tabuleiro_principal[teste_movimento][posicao2] == " ":
            possivel_ocupacao_linha = posicao1 + lista_pecas[peca].tipos_movimentos[0][0]
            possivel_ocupacao_coluna = posicao2 + lista_pecas[peca].tipos_movimentos[0][1]
            tabuleiro_principal[possivel_ocupacao_linha][possivel_ocupacao_coluna] = "•"
            tabuleiro_movimentos[possivel_ocupacao_linha][possivel_ocupacao_coluna] = "•"

            teste_movimento = posicao1 + lista_pecas[peca].tipos_movimentos[1][0]
            if str(teste_movimento) in "01234567" and str(posicao1) in "16" and tabuleiro_principal[teste_movimento][posicao2] == " ":
                possivel_ocupacao_linha = posicao1 + lista_pecas[peca].tipos_movimentos[1][0]
                possivel_ocupacao_coluna = posicao2 + lista_pecas[peca].tipos_movimentos[1][1]
                tabuleiro_principal[possivel_ocupacao_linha][possivel_ocupacao_coluna] = "•"
                tabuleiro_movimentos[possivel_ocupacao_linha][possivel_ocupacao_coluna] = "•"

        for c in range(2):
            teste_movimento1 = posicao1 + lista_pecas[peca].tipos_movimentos[2+c][0]
            teste_movimento2 = posicao2 + lista_pecas[peca].tipos_movimentos[2+c][1]
            global pos_passant1, pos_passant2
            print("a")
            print(pos_passant1, pos_passant2)
            print(posicao1, teste_movimento2)
            if str(teste_movimento1) not in "01234567" or str(teste_movimento2) not in "01234567":
                continue
            elif jogador_atual == True and descobrirPeca(teste_movimento1, teste_movimento2) in "♔♕♖♗♘♙" and tabuleiro_principal[teste_movimento1][teste_movimento2] != "":
                tabuleiro_movimentos[teste_movimento1][teste_movimento2] = "•"
                continue
            elif jogador_atual == False and descobrirPeca(teste_movimento1, teste_movimento2) in "♚♛♜♝♞♟" and tabuleiro_principal[teste_movimento1][teste_movimento2] != "":
                tabuleiro_movimentos[teste_movimento1][teste_movimento2] = "•"
                continue
            elif jogador_atual == True and pos_passant1 != 0 and pos_passant1 == posicao1 and pos_passant2 == teste_movimento2:
                tabuleiro_movimentos[teste_movimento1][teste_movimento2] = "•"
                tabuleiro_principal[teste_movimento1][teste_movimento2] = "•"
                pos_passant1 = teste_movimento1
                pos_passant2 = teste_movimento2
                print("b")
                continue
            elif jogador_atual == False and pos_passant1 != 0 and pos_passant1 == posicao1 and pos_passant2 == teste_movimento2:
                tabuleiro_movimentos[teste_movimento1][teste_movimento2] = "•"
                tabuleiro_principal[teste_movimento1][teste_movimento2] = "•"
                pos_passant1 = teste_movimento1
                pos_passant2 = teste_movimento2
                print("b")
                continue

    else:
        for movimento in lista_pecas[peca].tipos_movimentos:
            for multiplicador in range(10):
                if lista_pecas[peca].tipo_de_movimento == "INFINITO":
                    possivel_ocupacao_linha = posicao1 + movimento[0]*(multiplicador+1)
                    possivel_ocupacao_coluna = posicao2 + movimento[1]*(multiplicador+1)
                elif lista_pecas[peca].tipo_de_movimento == "UNICO":
                    possivel_ocupacao_linha = posicao1 + movimento[0]
                    possivel_ocupacao_coluna = posicao2 + movimento[1]
                if str(possivel_ocupacao_linha) not in "01234567" or str(possivel_ocupacao_coluna) not in "01234567":
                    break
                elif descobrirPeca(possivel_ocupacao_linha, possivel_ocupacao_coluna) == " ":
                    tabuleiro_principal[possivel_ocupacao_linha][possivel_ocupacao_coluna] = "•"
                    tabuleiro_movimentos[possivel_ocupacao_linha][possivel_ocupacao_coluna] = "•"
                elif descobrirPeca(possivel_ocupacao_linha, possivel_ocupacao_coluna) in "♔♕♖♗♘♙" and descobrirPeca(possivel_ocupacao_linha, possivel_ocupacao_coluna) != "" and jogador_atual == True or descobrirPeca(possivel_ocupacao_linha, possivel_ocupacao_coluna) in "♚♛♜♝♞♟" and descobrirPeca(possivel_ocupacao_linha, possivel_ocupacao_coluna) != "" and jogador_atual == False:
                    tabuleiro_movimentos[possivel_ocupacao_linha][possivel_ocupacao_coluna] = "•"
                    break
                else:
                    break
    return tabuleiro_movimentos

def mostrarMovimentosValidos(peca, posicao1, posicao2):
    tabuleiro_movimentos = []
    for c in range(len(lista_pecas)):
        if peca == lista_pecas[c].aparencia:
            tabuleiro_movimentos = descobrirMovimentosValidos(c, posicao1, posicao2)
    return tabuleiro_movimentos

def executarMovimento(peca, pos1, pos2, n_pos1, n_pos2):
    global pos_passant1, pos_passant2

    #execução caso en passant seja possivel
    if n_pos1 - pos1 == 2 and peca in "♙♟" or n_pos1 - pos1 == -2 and peca in "♙♟":
        print("en passant?")
        pos_passant1 = n_pos1
        pos_passant2 = n_pos2
    
    #execução caso o movimento escolhido seja de fato o en passant
    if tabuleiro_principal[n_pos1][n_pos2] == "•" and n_pos2 != pos2 and peca in "♙♟":
        if jogador_atual == True:
            tabuleiro_principal[n_pos1+1][n_pos2] = " "
        else:
            tabuleiro_principal[n_pos1-1][n_pos2] = " "

    #execução caso roque
    elif n_pos2 - pos2 == 2 and peca in "♔♚" or n_pos2 - pos2 == -2 and peca in "♔♚":
        if n_pos2 < 4:
            tabuleiro_principal[n_pos1][n_pos2-1] = " "
            tabuleiro_principal[n_pos1][n_pos2-2] = " "
            if jogador_atual == True:
                tabuleiro_principal[n_pos1][n_pos2+1] = "♜"
            else:
                tabuleiro_principal[n_pos1][n_pos2+1] = "♖"
        else:
            tabuleiro_principal[n_pos1][n_pos2+1] = " "
            if jogador_atual == True:
                tabuleiro_principal[n_pos1][n_pos2-1] = "♜"
            else:
                tabuleiro_principal[n_pos1][n_pos2-1] = "♖"

    tabuleiro_principal[n_pos1][n_pos2] = peca
    tabuleiro_principal[pos1][pos2] = " "

def limparMovimentosPossiveis(tabuleiro):
    for linha in range(8):
        for coluna in range(8):
            if tabuleiro[linha][coluna] == "•":
                tabuleiro[linha][coluna] = " "

def fimDeJogo(razao):
    if razao == "desistencia":
        if jogador_atual == True:
            print("=====================================================") 
            print("   FIM DE JOGO..\nAs Brancas desistiram, a vitória é das Pretas!! ♔")
            print("=====================================================") 
        else:
            print("=====================================================") 
            print("   FIM DE JOGO..\nAs Pretas desistiram, a vitória é das Brancas!! ♚")
            print("=====================================================") 

def turnoAtual(jogador):
    global jogador_atual, partida_rolando, pos_passant1, pos_passant2
    if jogador == True:
        print("- VEZ DAS BRANCAS ♚\n")
    else:
        print("- VEZ DAS PRETAS ♔\n")

    peca_escolhida = "aaaaaa"
    nova_posicao = "aaaaaaaa"
    se_peca_selecionada = False
    while se_peca_selecionada == False:
        imprimirTabuleiro(jogador)
        entrada_valida = False
        while entrada_valida == False:
            peca_escolhida = input("Digite as cordenadas da peça desejada (ex: b2 para selecionar ou b2b4 para selecionar e mover):\nVocê também pode desistir (desistir) se quiser\nResposta: ")
            if peca_escolhida.lower() == "desistir":
                partida_rolando = False
                fimDeJogo("desistencia")
                return
            elif len(peca_escolhida) == 2:
                if testarValidezCoordenada(peca_escolhida, False, tabuleiro_principal) == 0:
                    entrada_valida = True
                else:
                    imprimirValidezCoordenada(peca_escolhida, False, tabuleiro_principal)
                    continue
                se_peca_selecionada = True
                posicao1, posicao2 = descobrirPosicao(peca_escolhida)
                peca = descobrirPeca(posicao1, posicao2)
                tabuleiro_movimentos = mostrarMovimentosValidos(peca, posicao1, posicao2)
                imprimirTabuleiro(jogador)
            elif len(peca_escolhida) == 4:
                nova_posicao = peca_escolhida[2]+peca_escolhida[3]
                peca_escolhida = peca_escolhida[0]+peca_escolhida[1]
                if testarValidezCoordenada(peca_escolhida[0]+peca_escolhida[1], False, tabuleiro_principal) == 0:
                    entrada_valida = True
                else:
                    entrada_valida = False
                    peca_escolhida = "aaaaaa"
                    nova_posicao = "aaaaaaaa"
                    se_peca_selecionada = False
                    continue
                se_peca_selecionada = True
                posicao1, posicao2 = descobrirPosicao(peca_escolhida)
                peca = descobrirPeca(posicao1, posicao2)
                tabuleiro_movimentos = mostrarMovimentosValidos(peca, posicao1, posicao2)
                imprimirTabuleiro(jogador)
                if testarValidezCoordenada(nova_posicao, True, tabuleiro_movimentos) != 0:
                    entrada_valida = False
                    peca_escolhida = "aaaaaa"
                    nova_posicao = "aaaaaaaa"
                    se_peca_selecionada = False
                    limparMovimentosPossiveis(tabuleiro_principal)
                    imprimirTabuleiro(jogador_atual)
                    continue
                imprimirValidezCoordenada(peca_escolhida, False, tabuleiro_principal)
                imprimirValidezCoordenada(nova_posicao, True, tabuleiro_movimentos)
        print(testarValidezCoordenada(nova_posicao, True, tabuleiro_movimentos))
        while testarValidezCoordenada(nova_posicao, True, tabuleiro_movimentos) != 0 and se_peca_selecionada == True:
            nova_posicao = input("Para onde essa peça deve ir? (ex: b4)\nVocê também pode desistir (desistir) ou trocar de peça (trocar)\nResposta: ")
            if nova_posicao.lower() == "trocar":
                se_peca_selecionada = False
                peca_escolhida = "aaaaaaba"
                print("trocando a peça...")
                limparMovimentosPossiveis(tabuleiro_principal)
                break
            if nova_posicao.lower() == "desistir":
                partida_rolando = False
                fimDeJogo("desistencia")
                return
            imprimirValidezCoordenada(nova_posicao, True, tabuleiro_movimentos)
    nova_posicao1, nova_posicao2 = descobrirPosicao(nova_posicao)
    pos_passant1 = 0
    pos_passant2 = 0
    executarMovimento(peca, posicao1, posicao2, nova_posicao1, nova_posicao2)
    #print(pos_passant1, pos_passant2)
    #print(nova_posicao1, nova_posicao2)
    limparMovimentosPossiveis(tabuleiro_principal)
    imprimirTabuleiro(jogador)
    
    if jogador == True:
        jogador_atual = False
    else:
        jogador_atual = True
    if partida_rolando == True:
        turnoAtual(jogador_atual)
    else:
        print("A partida acabou...")
introducaoPartida()

""" 
"♔♕♖♗♘♙" 
"♚♛♜♝♞♟" 
""" 
