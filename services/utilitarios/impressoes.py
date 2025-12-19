from settings import settings
from services.utilitarios import turno_atual

def introduzirPartida():
    print("Que começem os Jogos..") 
    imprimirCabecalho("PARTIDA PADRÃO DE XADREZ")
    settings.partida_rolando = True
    settings.jogador_atual = True
    # turno_atual.turnoAtual(settings.jogador_atual)

def imprimirDivisoria():
    print("="*53)

def imprimirTitulo(titulo:str):
    novo_titulo = ""
    if len(titulo) <= 47:
        novo_titulo = adicionarEspacosNoTitulo(titulo)
    else:
        print("O título era muito grande. Escolha um menor.")
    novo_titulo = "=-" + novo_titulo + "-="
    print(novo_titulo)

def adicionarEspacosNoTitulo(titulo:str):
    novo_titulo = titulo
    adicionar_a_esquerda = True
    while len(novo_titulo) < 49:
        if adicionar_a_esquerda == True:
            novo_titulo = " " + novo_titulo
        else:
            novo_titulo = novo_titulo + " "
        adicionar_a_esquerda = not adicionar_a_esquerda
    return novo_titulo

def imprimirCabecalho(titulo:str):
    imprimirDivisoria()
    imprimirTitulo(titulo)
    imprimirDivisoria()
    print("\n")