from settings import settings
from models.enums_utilitarios import Jogador

def imprimirDeQuemEhAVezDeJogar():
    if settings.jogador_atual == Jogador.JOGADOR_DE_BRANCAS:
        imprimirTituloIsolado("- VEZ DAS BRANCAS ♚")
    elif settings.jogador_atual == Jogador.JOGADOR_DE_PRETAS:
        imprimirTituloIsolado("- VEZ DAS PRETAS ♔")

def imprimirTituloIsolado(titulo:str):
    print(f"\n\n\n{titulo}\n")

def introduzirPartida():
    print("Que começem os Jogos..") 
    imprimirCabecalho("PARTIDA PADRÃO DE XADREZ")

def imprimirCabecalho(titulo:str):
    imprimirDivisoria()
    imprimirTituloCabecalho(titulo)
    imprimirDivisoria()
    print("\n")

def imprimirCabecalhoComSubtitulo(titulo:str, subtitulo:str):
    imprimirDivisoria()
    imprimirTituloCabecalho(titulo)
    imprimirSubtituloCabecalho(subtitulo)
    imprimirDivisoria()

def imprimirDivisoria():
    print("="*53)

def imprimirTituloCabecalho(titulo:str):
    novo_titulo = formatarTextoParaPossuirQuantiaCaracteres(titulo, 47)
    novo_titulo = "=-" + novo_titulo + "-="
    print(novo_titulo)

def imprimirSubtituloCabecalho(subtitulo:str):
    novo_subtitulo = formatarTextoParaPossuirQuantiaCaracteres(subtitulo, 53)
    print(novo_subtitulo)

def formatarTextoParaPossuirQuantiaCaracteres(texto:str, quantia_caracteres:int):
    novo_texto = ""
    if len(texto) <= quantia_caracteres:
        novo_texto = adicionarEspacosNoTitulo(texto)
    else:
        print("O título era muito grande. Escolha um menor.")
    return novo_texto

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