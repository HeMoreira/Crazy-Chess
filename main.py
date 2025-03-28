import copy
numeros_tabuleiro = ["8","7","6","5","4","3","2","1"]
conversao_coluna = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}

class pecaXadrez:
    aparencia = ""
    tipos_movimentos = []
    time = True
    tipo_de_movimento = ""
    se_moveu = False
    #| UNICO | INFINITO | PEAO |
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

class movimentoPossivel:
    aparencia = "•"
movimento_possivel = movimentoPossivel()

class espacoVazio:
    aparencia = " "
espaco_vazio = espacoVazio()

#Criando Objetos das peças do tabuleiro
"""
tabuleiro_principal = [
    [torre(False, "♖"), cavalo(False, "♘"), bispo(False, "♗"), rainha(False, "♕"), rei(False, "♔"), bispo(False, "♗"), cavalo(False, "♘"), torre(False, "♖")],
    [peao(False, "♙"), peao(False, "♙"), peao(False, "♙"), peao(False, "♙"), peao(False, "♙"), peao(False, "♙"), peao(False, "♙"), peao(False, "♙")],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [peao(True, "♟"), peao(True, "♟"), peao(True, "♟"), peao(True, "♟"), peao(True, "♟"), peao(True, "♟"), peao(True, "♟"), peao(True, "♟")],
    [torre(True, "♜"), cavalo(True, "♞"), bispo(True, "♝"), rainha(True, "♛"), rei(True, "♚"), bispo(True, "♝"),cavalo(True, "♞"), torre(True, "♜")]
]
"""
tabuleiro_principal = [
    [torre(False, "♖"), espaco_vazio, espaco_vazio, espaco_vazio, rei(False, "♔"), espaco_vazio, espaco_vazio, torre(False, "♖")],
    [peao(True, "♟"), peao(True, "♟"), peao(True, "♟"), peao(True, "♟"), peao(True, "♟"), peao(True, "♟"), peao(True, "♟"), peao(True, "♟")],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [peao(False, "♙"), peao(False, "♙"), peao(False, "♙"), peao(False, "♙"), peao(False, "♙"), peao(False, "♙"), peao(False, "♙"), peao(False, "♙")],
    [torre(True, "♜"), espaco_vazio, espaco_vazio, espaco_vazio, rei(True, "♚"), espaco_vazio, espaco_vazio, torre(True, "♜")]
]
#"""
#lista_pecas = [bispo_preto, bispo_branco, torre_preto, torre_branco, cavalo_preto, cavalo_branco, rainha_preto, rainha_branco, rei_preto, rei_branco, peao_preto, peao_branco]
 
#BRANCAS = TRUE, PRETAS = FALSE
partida_rolando = True
jogador_atual = True

def imprimirTabuleiro(jogador): 
    impressao = ""
    tabuleiro_suporte = copy.deepcopy(tabuleiro_principal)
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
            impressao = impressao + " |" + tabuleiro_suporte[linha][coluna].aparencia
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
    turnoAtual(jogador_atual)

def descobrirPeca(posicao1, posicao2):
    return tabuleiro_principal[posicao1][posicao2]

def testarValidezPeca(peca, se_nova_posicao):
    if peca.aparencia == " " and se_nova_posicao == False:
        return 3
    elif peca.aparencia in "♔♕♖♗♘♙" and peca.aparencia != "" and jogador_atual == True and se_nova_posicao == False:
        return 4
    elif peca.aparencia in "♚♛♜♝♞♟" and peca.aparencia != "" and jogador_atual == False and se_nova_posicao == False:
        return 4
    elif se_nova_posicao == True and peca.aparencia != "•":
        return 5
    else:
        return 0

def testarValidezCoordenada(entrada, se_nova_posicao, tabuleiro):
    posicao1, posicao2 = descobrirPosicao(entrada)
    if posicao1 == -1:
        return 2
    else:
        peca = None
        peca = tabuleiro[posicao1][posicao2]
        return testarValidezPeca(peca, se_nova_posicao)

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
        tabuleiro[i] = [espaco_vazio]*8
    return tabuleiro

def descobrirMovimentosValidos(peca, posicao1, posicao2):
    tabuleiro_movimentos = novoTabuleiroVazio()
    if peca.tipo_de_movimento == "PEAO":

        teste_movimento = posicao1 + peca.tipos_movimentos[0][0]
        if str(teste_movimento) in "01234567" and tabuleiro_principal[teste_movimento][posicao2].aparencia == " ":
            possivel_ocupacao_linha = posicao1 + peca.tipos_movimentos[0][0]
            possivel_ocupacao_coluna = posicao2 + peca.tipos_movimentos[0][1]
            tabuleiro_principal[possivel_ocupacao_linha][possivel_ocupacao_coluna] = movimento_possivel
            tabuleiro_movimentos[possivel_ocupacao_linha][possivel_ocupacao_coluna] = movimento_possivel

            teste_movimento = posicao1 + peca.tipos_movimentos[1][0]
            if str(teste_movimento) in "01234567" and str(posicao1) in "16" and tabuleiro_principal[teste_movimento][posicao2].aparencia == " ":
                possivel_ocupacao_linha = posicao1 + peca.tipos_movimentos[1][0]
                possivel_ocupacao_coluna = posicao2 + peca.tipos_movimentos[1][1]
                tabuleiro_principal[possivel_ocupacao_linha][possivel_ocupacao_coluna] = movimento_possivel
                tabuleiro_movimentos[possivel_ocupacao_linha][possivel_ocupacao_coluna] = movimento_possivel

        for c in range(2):
            teste_movimento1 = posicao1 + peca.tipos_movimentos[2+c][0]
            teste_movimento2 = posicao2 + peca.tipos_movimentos[2+c][1]
            if str(teste_movimento1) not in "01234567" or str(teste_movimento2) not in "01234567":
                continue
            elif jogador_atual == True and descobrirPeca(teste_movimento1, teste_movimento2).aparencia in "♔♕♖♗♘♙" and tabuleiro_principal[teste_movimento1][teste_movimento2].aparencia != "":
                tabuleiro_movimentos[teste_movimento1][teste_movimento2] = movimento_possivel
                continue
            elif jogador_atual == False and descobrirPeca(teste_movimento1, teste_movimento2).aparencia in "♚♛♜♝♞♟" and tabuleiro_principal[teste_movimento1][teste_movimento2].aparencia != "":
                tabuleiro_movimentos[teste_movimento1][teste_movimento2] = movimento_possivel
                continue
            elif descobrirPeca(posicao1, posicao2).passant_direita == True and c == 1 or descobrirPeca(posicao1, posicao2).passant_esquerda == True and c == 0:
                tabuleiro_movimentos[teste_movimento1][teste_movimento2] = movimento_possivel
                tabuleiro_principal[teste_movimento1][teste_movimento2] = movimento_possivel
                continue

    else:
        for movimento in peca.tipos_movimentos:
            for multiplicador in range(10):
                if peca.tipo_de_movimento == "INFINITO":
                    possivel_ocupacao_linha = posicao1 + movimento[0]*(multiplicador+1)
                    possivel_ocupacao_coluna = posicao2 + movimento[1]*(multiplicador+1)
                elif peca.tipo_de_movimento == "UNICO":
                    possivel_ocupacao_linha = posicao1 + movimento[0]
                    possivel_ocupacao_coluna = posicao2 + movimento[1]
                print("a")
                if str(possivel_ocupacao_linha) not in "01234567" or str(possivel_ocupacao_coluna) not in "01234567":
                    break
                elif peca.aparencia in "♔♚" and movimento == peca.tipos_movimentos[8] and descobrirPeca(posicao1, 7).aparencia in "♖♜":
                    if peca.se_moveu == False and descobrirPeca(posicao1, 7).se_moveu == False and descobrirPeca(posicao1, 6).aparencia in "• " and descobrirPeca(posicao1, 5).aparencia in "• ":
                        tabuleiro_principal[possivel_ocupacao_linha][possivel_ocupacao_coluna] = movimento_possivel
                        tabuleiro_movimentos[possivel_ocupacao_linha][possivel_ocupacao_coluna] = movimento_possivel
                        break
                elif peca.aparencia in "♔♚" and movimento == peca.tipos_movimentos[9] and descobrirPeca(posicao1, 0).aparencia in "♖♜":
                    if peca.se_moveu == False and descobrirPeca(posicao1, 0).se_moveu == False and descobrirPeca(posicao1, 1).aparencia in "• " and descobrirPeca(posicao1, 2).aparencia in "• " and descobrirPeca(posicao1, 3).aparencia in "• ":
                        tabuleiro_principal[possivel_ocupacao_linha][possivel_ocupacao_coluna] = movimento_possivel
                        tabuleiro_movimentos[possivel_ocupacao_linha][possivel_ocupacao_coluna] = movimento_possivel
                        break
                elif descobrirPeca(possivel_ocupacao_linha, possivel_ocupacao_coluna).aparencia == " ":
                    tabuleiro_principal[possivel_ocupacao_linha][possivel_ocupacao_coluna] = movimento_possivel
                    tabuleiro_movimentos[possivel_ocupacao_linha][possivel_ocupacao_coluna] = movimento_possivel
                elif descobrirPeca(possivel_ocupacao_linha, possivel_ocupacao_coluna).aparencia in "♔♕♖♗♘♙" and descobrirPeca(possivel_ocupacao_linha, possivel_ocupacao_coluna).aparencia != "" and jogador_atual == True or descobrirPeca(possivel_ocupacao_linha, possivel_ocupacao_coluna).aparencia in "♚♛♜♝♞♟" and descobrirPeca(possivel_ocupacao_linha, possivel_ocupacao_coluna).aparencia != "" and jogador_atual == False:
                    tabuleiro_movimentos[possivel_ocupacao_linha][possivel_ocupacao_coluna] = movimento_possivel
                    break
                else:
                    break
    limparPassantsPossiveis(tabuleiro_principal)
    return tabuleiro_movimentos

def mostrarMovimentosValidos(peca, posicao1, posicao2):
    tabuleiro_movimentos = []
    for c in range(8):
        for i in range(8):
            if peca == tabuleiro_principal[c][i]:
                tabuleiro_movimentos = descobrirMovimentosValidos(peca, posicao1, posicao2)
    return tabuleiro_movimentos

def executarMovimento(peca, pos1, pos2, n_pos1, n_pos2):

    #execução caso en passant seja possivel
    if n_pos1 - pos1 == 2 and peca.aparencia == "♙" or n_pos1 - pos1 == -2 and peca.aparencia == "♟":
        if n_pos1 - pos1 == 2 and descobrirPeca(n_pos1, n_pos2-1).aparencia == "♟":
            descobrirPeca(n_pos1, n_pos2-1).passant_direita = True
        if n_pos1 - pos1 == 2 and descobrirPeca(n_pos1, n_pos2+1).aparencia == "♟":
            descobrirPeca(n_pos1, n_pos2+1).passant_esquerda = True
        if n_pos1 - pos1 == -2 and descobrirPeca(n_pos1, n_pos2-1).aparencia == "♙":
            descobrirPeca(n_pos1, n_pos2-1).passant_direita = True
        if n_pos1 - pos1 == -2 and descobrirPeca(n_pos1, n_pos2+1).aparencia == "♙":
            descobrirPeca(n_pos1, n_pos2+1).passant_esquerda = True
    
    #execução caso o movimento escolhido seja de fato o en passant
    if tabuleiro_principal[n_pos1][n_pos2].aparencia == "•" and n_pos2 != pos2 and peca.aparencia in "♙♟":
        if jogador_atual == True:
            tabuleiro_principal[n_pos1+1][n_pos2] = espaco_vazio
        else:
            tabuleiro_principal[n_pos1-1][n_pos2] = espaco_vazio

    #execução caso o peão movido esteja na linha de promoção
    if peca.aparencia == "♙" and n_pos1 == 7 or peca.aparencia == "♟" and n_pos1 == 0:
        peca.promovido = True

    #execução caso roque
    elif n_pos2 - pos2 == 2 and peca.aparencia in "♔♚" and peca.se_moveu == False or n_pos2 - pos2 == -2 and peca.aparencia in "♔♚" and peca.se_moveu == False:
        if n_pos2 < 4:
            tabuleiro_principal[n_pos1][n_pos2+1] = tabuleiro_principal[n_pos1][n_pos2-2]
            tabuleiro_principal[n_pos1][n_pos2-2] = espaco_vazio
        else:
            tabuleiro_principal[n_pos1][n_pos2-1] = tabuleiro_principal[n_pos1][n_pos2+1]
            tabuleiro_principal[n_pos1][n_pos2+1] = espaco_vazio
            

    #execução padrão e geral do movimento
    if peca.se_moveu == False:
        peca.se_moveu = True
    tabuleiro_principal[n_pos1][n_pos2] = peca
    tabuleiro_principal[pos1][pos2] = espaco_vazio

def limparMovimentosPossiveis(tabuleiro):
    for linha in range(8):
        for coluna in range(8):
            if tabuleiro[linha][coluna] == movimento_possivel:
                tabuleiro[linha][coluna] = espaco_vazio

def limparPassantsPossiveis(tabuleiro):
    for linha in range(8):
        for coluna in range(8):
            if tabuleiro[linha][coluna].aparencia in "♟♙":
                tabuleiro[linha][coluna].passant_direita = False
                tabuleiro[linha][coluna].passant_esquerda = False

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

def PromoverPeao(peca, pos1, pos2):
    print("=====================================================")
    print("                -= PROMOÇÃO DE PEÃO =-               ")
    print("=====================================================")
    imprimirTabuleiro(tabuleiro_principal)
    print("=====================================================")
    print("Que aventura em.. deseja trocar seu peão por qual peça?")
    promocao = "aaaaaaaaaaaa"
    while promocao != "cavalo" and promocao != "bispo" and promocao != "torre" and promocao != "rainha":
        promocao = input("Resposta: ")
        promocao = promocao.lower()
        if promocao == "cavalo":
            if peca.time == True:
                tabuleiro_principal[pos1][pos2] = cavalo(True, "♞")
            else:
                tabuleiro_principal[pos1][pos2] = cavalo(False, "♘")
        elif promocao == "torre":
            if peca.time == True:
                tabuleiro_principal[pos1][pos2] = torre(True, "♜")
            else:
                tabuleiro_principal[pos1][pos2] = torre(False, "♖")
        elif promocao == "bispo":
            if peca.time == True:
                tabuleiro_principal[pos1][pos2] = bispo(True, "♝")
            else:
                tabuleiro_principal[pos1][pos2] = bispo(False, "♗")
        elif promocao == "rainha":
            if peca.time == True:
                tabuleiro_principal[pos1][pos2] = rainha(True, "♛")
            else:
                tabuleiro_principal[pos1][pos2] = rainha(False, "♕")
        else:
            print("Entrada Inválida, certifique-se de escrever o nome correto da peça...")
    print("=====================================================")
    print(f"{tabuleiro_principal[pos1][pos2].aparencia} - Seu peão foi promovido para {promocao}!!")
    print("=====================================================")

def turnoAtual(jogador):
    global jogador_atual, partida_rolando
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
        #print(testarValidezCoordenada(nova_posicao, True, tabuleiro_movimentos))
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
    executarMovimento(peca, posicao1, posicao2, nova_posicao1, nova_posicao2)
    limparMovimentosPossiveis(tabuleiro_principal)
    if peca.aparencia in "♙♟":
        if peca.promovido == True:
            PromoverPeao(peca, nova_posicao1, nova_posicao2)
        else:
            imprimirTabuleiro(jogador)
    else:
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
