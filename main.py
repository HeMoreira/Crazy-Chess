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
#"""
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
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, rei(False, "♔"), espaco_vazio, espaco_vazio, espaco_vazio],
    [peao(True, "♟"), peao(True, "♟"), peao(True, "♟"), espaco_vazio, espaco_vazio, espaco_vazio, peao(True, "♟"), peao(True, "♟")],
    [espaco_vazio, espaco_vazio, peao(True, "♟"), peao(True, "♟"), espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [espaco_vazio, espaco_vazio, espaco_vazio, rei(True, "♚"), espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio],
    [torre(True, "♜"), espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, torre(True, "♜")]
]
#"""

#BRANCAS = TRUE, PRETAS = FALSE
partida_rolando = True
jogador_atual = True

def imprimirTabuleiro(jogador): 
    impressao = ""
    tabuleiro_suporte = copy.deepcopy(tabuleiro_principal)
    numeros_tabuleiro_suporte = numeros_tabuleiro
    #Inversão dinâmica do tabuleiro conforme o jogador
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
    print("-=             PARTIDA PADRÃO DE XADREZ            =-") 
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
            print("! Coordenada Inválida, as coordenadas só podem ter 2 ou 4 caractéres..")
        elif testarValidezCoordenada(entrada, se_nova_posicao, tabuleiro) == 2:
            print("! Coordenada Inválida, digite as coordenadas no formato de [coluna][linha]..")
        elif testarValidezCoordenada(entrada, se_nova_posicao, tabuleiro) == 3:
            print("! Coordenada Inválida, Não tem nenhuma peça nessa posição..")
        elif testarValidezCoordenada(entrada, se_nova_posicao, tabuleiro) == 4:
            print("! Coordenada Inválida, você não pode mover esta peça..")
        elif testarValidezCoordenada(entrada, se_nova_posicao, tabuleiro) == 5:
            print("! Coordenada Inválida, esta peça não pode ir para esta posição..")
        elif testarValidezCoordenada(entrada, se_nova_posicao, tabuleiro) == 6:
            print("! Coordenada Inválida, alguma das informações digitadas não foi aceita..")
        return 0
    else:
        return 1

def novoTabuleiroVazio():
    tabuleiro = [[],[],[],[],[],[],[],[]]
    for i in range(8):
        tabuleiro[i] = [espaco_vazio]*8
    return tabuleiro

def descobrirMovimentosValidos(peca, posicao1, posicao2, jogador):
    tabuleiro_movimentos = novoTabuleiroVazio()
    if peca.tipo_de_movimento == "PEAO":

        teste_movimento = posicao1 + peca.tipos_movimentos[0][0]
        if str(teste_movimento) in "01234567" and tabuleiro_principal[teste_movimento][posicao2].aparencia in "• ":
            possivel_ocupacao_linha = posicao1 + peca.tipos_movimentos[0][0]
            possivel_ocupacao_coluna = posicao2 + peca.tipos_movimentos[0][1]
            tabuleiro_principal[possivel_ocupacao_linha][possivel_ocupacao_coluna] = movimento_possivel
            tabuleiro_movimentos[possivel_ocupacao_linha][possivel_ocupacao_coluna] = movimento_possivel

            teste_movimento = posicao1 + peca.tipos_movimentos[1][0]
            if str(teste_movimento) in "01234567" and str(posicao1) in "16" and tabuleiro_principal[teste_movimento][posicao2].aparencia in "• ":
                possivel_ocupacao_linha = posicao1 + peca.tipos_movimentos[1][0]
                possivel_ocupacao_coluna = posicao2 + peca.tipos_movimentos[1][1]
                tabuleiro_principal[possivel_ocupacao_linha][possivel_ocupacao_coluna] = movimento_possivel
                tabuleiro_movimentos[possivel_ocupacao_linha][possivel_ocupacao_coluna] = movimento_possivel

        for c in range(2):
            teste_movimento1 = posicao1 + peca.tipos_movimentos[2+c][0]
            teste_movimento2 = posicao2 + peca.tipos_movimentos[2+c][1]
            if str(teste_movimento1) not in "01234567" or str(teste_movimento2) not in "01234567":
                continue
            elif jogador == True and descobrirPeca(teste_movimento1, teste_movimento2).aparencia in "♔♕♖♗♘♙" and tabuleiro_principal[teste_movimento1][teste_movimento2].aparencia != "":
                tabuleiro_movimentos[teste_movimento1][teste_movimento2] = movimento_possivel
                continue
            elif jogador == False and descobrirPeca(teste_movimento1, teste_movimento2).aparencia in "♚♛♜♝♞♟" and tabuleiro_principal[teste_movimento1][teste_movimento2].aparencia != "":
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
                if str(possivel_ocupacao_linha) not in "01234567" or str(possivel_ocupacao_coluna) not in "01234567":
                    break
                elif peca.aparencia in "♔♚" and movimento == peca.tipos_movimentos[8] or peca.aparencia in "♔♚" and movimento == peca.tipos_movimentos[9]:
                    if peca.aparencia in "♔♚" and movimento == peca.tipos_movimentos[8] and descobrirPeca(posicao1, 7).aparencia in "♖♜" or peca.aparencia in "♔♚" and movimento == peca.tipos_movimentos[9] and descobrirPeca(posicao1, 0).aparencia in "♖♜":
                        if peca.se_moveu == False and descobrirPeca(posicao1, 7).se_moveu == False and descobrirPeca(posicao1, 7).time == peca.time and descobrirPeca(posicao1, 6).aparencia in "• " and descobrirPeca(posicao1, 5).aparencia in "• ":
                            tabuleiro_principal[possivel_ocupacao_linha][possivel_ocupacao_coluna] = movimento_possivel
                            tabuleiro_movimentos[possivel_ocupacao_linha][possivel_ocupacao_coluna] = movimento_possivel
                        if peca.se_moveu == False and descobrirPeca(posicao1, 0).se_moveu == False and descobrirPeca(posicao1, 0).time == peca.time and descobrirPeca(posicao1, 1).aparencia in "• " and descobrirPeca(posicao1, 2).aparencia in "• " and descobrirPeca(posicao1, 3).aparencia in "• ":
                            tabuleiro_principal[possivel_ocupacao_linha][possivel_ocupacao_coluna] = movimento_possivel
                            tabuleiro_movimentos[possivel_ocupacao_linha][possivel_ocupacao_coluna] = movimento_possivel
                    break
                elif descobrirPeca(possivel_ocupacao_linha, possivel_ocupacao_coluna).aparencia in "• ":
                    tabuleiro_principal[possivel_ocupacao_linha][possivel_ocupacao_coluna] = movimento_possivel
                    tabuleiro_movimentos[possivel_ocupacao_linha][possivel_ocupacao_coluna] = movimento_possivel
                elif descobrirPeca(possivel_ocupacao_linha, possivel_ocupacao_coluna).aparencia in "♔♕♖♗♘♙" and descobrirPeca(possivel_ocupacao_linha, possivel_ocupacao_coluna).aparencia != "" and jogador == True or descobrirPeca(possivel_ocupacao_linha, possivel_ocupacao_coluna).aparencia in "♚♛♜♝♞♟" and descobrirPeca(possivel_ocupacao_linha, possivel_ocupacao_coluna).aparencia != "" and jogador == False:
                    tabuleiro_movimentos[possivel_ocupacao_linha][possivel_ocupacao_coluna] = movimento_possivel
                    break
                else:
                    break
    return tabuleiro_movimentos

def mostrarMovimentosValidos(peca, posicao1, posicao2, jogador):
    tabuleiro_movimentos = []
    for c in range(8):
        for i in range(8):
            if peca == tabuleiro_principal[c][i]:
                tabuleiro_movimentos = descobrirMovimentosValidos(peca, posicao1, posicao2, jogador)
    return tabuleiro_movimentos

def executarMovimento(peca, pos1, pos2, n_pos1, n_pos2):

    #execução caso o movimento escolhido seja de fato o en passant
    if tabuleiro_principal[n_pos1][n_pos2].aparencia == "•" and n_pos2 != pos2 and peca.aparencia in "♙♟":
        if jogador_atual == True:
            tabuleiro_principal[n_pos1+1][n_pos2] = espaco_vazio
        else:
            tabuleiro_principal[n_pos1-1][n_pos2] = espaco_vazio
            
    limparPassantsPossiveis(tabuleiro_principal)

    #execução caso en passant seja possivel
    if n_pos1 - pos1 == 2 and peca.aparencia == "♙" or n_pos1 - pos1 == -2 and peca.aparencia == "♟":
        if n_pos1 - pos1 == 2 and n_pos2-1 >= 0:
            if descobrirPeca(n_pos1, n_pos2-1).aparencia == "♟":
                descobrirPeca(n_pos1, n_pos2-1).passant_direita = True
        if n_pos1 - pos1 == 2 and n_pos2+1 < 8:
            if descobrirPeca(n_pos1, n_pos2+1).aparencia == "♟":
                descobrirPeca(n_pos1, n_pos2+1).passant_esquerda = True
        if n_pos1 - pos1 == -2 and n_pos2-1 >= 0:
            if descobrirPeca(n_pos1, n_pos2-1).aparencia == "♙":
                descobrirPeca(n_pos1, n_pos2-1).passant_direita = True
        if n_pos1 - pos1 == -2 and n_pos2+1 < 8:
            if descobrirPeca(n_pos1, n_pos2+1).aparencia == "♙":
                descobrirPeca(n_pos1, n_pos2+1).passant_esquerda = True

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
    peca.se_moveu = True
    tabuleiro_principal[n_pos1][n_pos2] = peca
    tabuleiro_principal[pos1][pos2] = espaco_vazio

def limparMovimentosPossiveis(tabuleiro):
    for linha in range(8):
        for coluna in range(8):
            if tabuleiro[linha][coluna].aparencia == "•":
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
    if razao == "cheque-mate":
        if jogador_atual == True:
            print("=====================================================") 
            print("   FIM DE JOGO..\nO rei Branco foi encurralado, a vitória é das Pretas!! ♔")
            print("=====================================================") 
        else:
            print("=====================================================") 
            print("   FIM DE JOGO..\nO rei Preto foi encurralado, a vitória é das Brancas!! ♚")
            print("=====================================================")
    if razao == "afogamento":
        print("=====================================================") 
        print("   FIM DE JOGO..\nUm dos jogadores não pode jogar, o empate é forçado!! #")
        print("=====================================================")
    if razao == "empate":
        print("=====================================================") 
        print("   FIM DE JOGO..\nQue partida! Os jogadores negociaram um empate!! #")
        print("=====================================================")

def PromoverPeao(peca, pos1, pos2):
    print("=====================================================")
    print("                -= PROMOÇÃO DE PEÃO =-               ")
    print("=====================================================")
    imprimirTabuleiro(tabuleiro_principal)
    print("=====================================================")
    print("Que aventura em.. deseja trocar seu peão por qual peça?\nVocê pode escolher entre 'cavalo', 'torre', 'bispo', e 'rainha'")
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
            print("! Entrada Inválida, certifique-se de escrever o nome correto da peça...")
    print("=====================================================")
    print(f"{tabuleiro_principal[pos1][pos2].aparencia} - Seu peão foi promovido para {promocao}!!")
    print("=====================================================")

def testarCheque():
    global jogador_atual, partida_rolando, tabuleiro_principal
    for linha in range(8):
        for coluna in range(8):
            peca = descobrirPeca(linha, coluna)
            if jogador_atual == True and peca.aparencia in "♔♕♖♗♘♙" or jogador_atual == False and peca.aparencia in "♚♛♜♝♞♟":
                if jogador_atual == True:
                    tabuleiro_movimentos = descobrirMovimentosValidos(peca, linha, coluna, False)
                else:
                    tabuleiro_movimentos = descobrirMovimentosValidos(peca, linha, coluna, True)
                for linha2 in range(8):
                    for coluna2 in range(8):
                        if tabuleiro_movimentos[linha2][coluna2].aparencia == "•":
                            if jogador_atual == True and tabuleiro_principal[linha2][coluna2].aparencia == "♚" or jogador_atual == False and tabuleiro_principal[linha2][coluna2].aparencia == "♔":
                                limparMovimentosPossiveis(tabuleiro_principal)
                                return True
    limparMovimentosPossiveis(tabuleiro_principal)
    return False

def testarChequeMate():
    global jogador_atual, partida_rolando, tabuleiro_principal
    em_cheque = True
    quant_movimentos_possiveis = 0
    if testarCheque() == False:
        em_cheque = False
    for linha in range(8):
        for coluna in range(8):
            peca = descobrirPeca(linha, coluna)
            if jogador_atual == False and peca.aparencia in "♔♕♖♗♘♙" or jogador_atual == True and peca.aparencia in "♚♛♜♝♞♟":
                tabuleiro_movimentos = descobrirMovimentosValidos(peca, linha, coluna, jogador_atual)
                for linha2 in range(8):
                    for coluna2 in range(8):
                        if tabuleiro_movimentos[linha2][coluna2].aparencia == "•":
                            limparMovimentosPossiveis(tabuleiro_principal)
                            tabuleiro_suporte = copy.deepcopy(tabuleiro_principal)
                            executarMovimento(peca, linha, coluna, linha2, coluna2)
                            if testarCheque() == False and em_cheque == False:
                                tabuleiro_principal = copy.deepcopy(tabuleiro_suporte)
                                quant_movimentos_possiveis+=1
                                print(quant_movimentos_possiveis)
                            if testarCheque() == True:
                                tabuleiro_principal = copy.deepcopy(tabuleiro_suporte)
                            elif testarCheque() == False:
                                tabuleiro_principal = copy.deepcopy(tabuleiro_suporte)
                                return "CHEQUE"
    if quant_movimentos_possiveis == 0 and testarCheque() == False:
        return "AFOGAMENTO"
    return "MATE"

def tentativaEmpate():
    print("=====================================================") 
    print("             -= ! PROPOSTA DE EMPATE ! =-            ")
    print("      Seu oponente propôs empate, você aceita?       ")
    print("=====================================================")
    resposta = "aaaa"
    while resposta.lower() != "sim" and resposta.lower() != "nao" and resposta.lower() != "não":
        resposta = input("Responda 'SIM' ou 'NÃO' conforme a sua resposta\nResposta: ")
    return resposta.lower()

def turnoAtual(jogador):
    global jogador_atual, partida_rolando, tabuleiro_principal
    if jogador == True:
        print("\n\n\n\n- VEZ DAS BRANCAS ♚\n")
    else:
        print("\n\n\n\n- VEZ DAS PRETAS ♔\n")
    while True:
        if testarChequeMate() == "MATE":
            print("=====================================================") 
            print("                 -= ! CHEQUE MATE ! =-               ")
            print("  Seu rei foi encurralado, esse é o fim para você..  ")
            print("=====================================================")
            imprimirTabuleiro(jogador)
            partida_rolando = False
            fimDeJogo("cheque-mate")
            return
        elif testarChequeMate() == "AFOGAMENTO":
            print("=====================================================") 
            print("                 -= ! AFOGAMENTO ! =-                ")
            print("  Você não é capaz de passar a vez, empate forçado!  ")
            print("=====================================================")
            imprimirTabuleiro(jogador)
            partida_rolando = False
            fimDeJogo("afogamento")
            return
        elif testarCheque() == True:
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
                imprimirTabuleiro(jogador)
                entrada_valida = False
                while entrada_valida == False:
                    print("==========================================================================================================") 
                    peca_escolhida = input("Digite as cordenadas da peça desejada (ex: b2 para selecionar ou b2b4 para selecionar e mover):\nVocê também pode desistir (desistir) ou pedir por empate (empate) se quiser\nResposta: ")
                    if peca_escolhida.lower() == "desistir":
                        partida_rolando = False
                        fimDeJogo("desistencia")
                        return
                    if peca_escolhida.lower() == "empate":
                        resposta = tentativaEmpate()
                        if resposta == "sim":
                            partida_rolando = False
                            fimDeJogo("empate")
                            return
                        elif resposta == "nao" or resposta == "não":
                            print("=====================================================") 
                            print("            O pedido de EMPATE foi NEGADO!           ")
                            print("    Alguém está confiante.. a partida continua!!     ")
                            print("=====================================================")
                            continue
                    elif len(peca_escolhida) == 2:
                        if testarValidezCoordenada(peca_escolhida, False, tabuleiro_principal) == 0:
                            entrada_valida = True
                        else:
                            imprimirValidezCoordenada(peca_escolhida, False, tabuleiro_principal)
                            continue
                        se_peca_selecionada = True
                        posicao1, posicao2 = descobrirPosicao(peca_escolhida)
                        peca = descobrirPeca(posicao1, posicao2)
                        tabuleiro_movimentos = mostrarMovimentosValidos(peca, posicao1, posicao2, jogador_atual)
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
                        tabuleiro_movimentos = mostrarMovimentosValidos(peca, posicao1, posicao2, jogador_atual)
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
                while testarValidezCoordenada(nova_posicao, True, tabuleiro_movimentos) != 0 and se_peca_selecionada == True:
                    print("==========================================================================================================") 
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
            tabuleiro_suporte = copy.deepcopy(tabuleiro_principal)
            limparMovimentosPossiveis(tabuleiro_suporte)
            nova_posicao1, nova_posicao2 = descobrirPosicao(nova_posicao)
            executarMovimento(peca, posicao1, posicao2, nova_posicao1, nova_posicao2)
            if testarCheque() == False:
                limparMovimentosPossiveis(tabuleiro_principal)
            else:
                tabuleiro_principal = copy.deepcopy(tabuleiro_suporte)
                limparMovimentosPossiveis(tabuleiro_principal)
                print("Você não pode deixar seu rei ser derrotado.. Faça outro movimento!")
                abortar = True
                tabuleiro_principal = copy.deepcopy(tabuleiro_suporte)
                se_peca_selecionada = False
                peca_escolhida = "aaaaaaba"
                nova_posicao = "bbbbbbbbab"
                continue
                limparMovimentosPossiveis(tabuleiro_principal)
            if peca.aparencia in "♙♟":
                if peca.promovido == True:
                    PromoverPeao(peca, nova_posicao1, nova_posicao2)
            imprimirTabuleiro(jogador)
            confirmacao = "aaaaa"
            while confirmacao.lower() != "" and confirmacao.lower() != "cancelar":
                confirmacao = input("Confirme o movimento pressione enter ou retroceda digitando 'cancelar': ")
            if confirmacao.lower() == "cancelar":
                abortar = True
                tabuleiro_principal = copy.deepcopy(tabuleiro_suporte)
                se_peca_selecionada = False
                peca_escolhida = "aaaaaaba"
                nova_posicao = "bbbbbbbbab"
                print("Refazendo movimento...")
                limparMovimentosPossiveis(tabuleiro_principal)
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
