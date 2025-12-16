from settings import settings

def fimDeJogo(razao):
    if razao == "desistencia":
        if settings.jogador_atual == True:
            print("=====================================================") 
            print("   FIM DE JOGO..\nAs Brancas desistiram, a vitória é das Pretas!! ♔")
            print("=====================================================") 
        else:
            print("=====================================================") 
            print("   FIM DE JOGO..\nAs Pretas desistiram, a vitória é das Brancas!! ♚")
            print("=====================================================")
    if razao == "cheque-mate":
        if settings.jogador_atual == True:
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

def tentativaEmpate():
    print("=====================================================") 
    print("             -= ! PROPOSTA DE EMPATE ! =-            ")
    print("      Seu oponente propôs empate, você aceita?       ")
    print("=====================================================")
    resposta = "aaaa"
    while resposta.lower() != "sim" and resposta.lower() != "nao" and resposta.lower() != "não":
        resposta = input("Responda 'SIM' ou 'NÃO' conforme a sua resposta\nResposta: ")
    return resposta.lower()