from settings import settings
from models.cords import Cordenadas
from models.peca_xadrez import PecaXadrez
from services.utilitarios import impressoes
from services.tabuleiro import tabuleiros


def descobrirPeca(cordenadas:Cordenadas):
    return settings.tabuleiro_principal[cordenadas.indice_linha][cordenadas.indice_coluna]

def promoverPeaoSeEmCasaDePromocao(peca:PecaXadrez):
    if peca.classe == "peao":
        if peca.promovido == True:
            promoverPeao(peca)

def promoverPeao(peca:PecaXadrez):
    impressoes.imprimirCabecalho("PROMOÇÃO DE PEÃO")
    tabuleiros.imprimirTabuleiro(settings.tabuleiro_principal)
    impressoes.imprimirDivisoria()
    print("Que aventura em.. deseja promover seu peão para qual peça?\nVocê pode escolher entre 'cavalo', 'torre', 'bispo', e 'rainha'")
    
    peca = selecionarPromocaoDoPeao(peca)

    impressoes.imprimirDivisoria()
    print(f"{peca.aparencia} - Seu peão foi promovido para {peca.classe}!!")
    impressoes.imprimirDivisoria()

def selecionarPromocaoDoPeao(peca:PecaXadrez):
    promocao = "entrada inválida"
    while promocao not in ["cavalo", "torre", "bispo", "rainha"]:
        promocao = input("Resposta: ").lower().strip()
        if promocao not in ["cavalo", "torre", "bispo", "rainha"]:
            print("! Entrada Inválida, certifique-se de escrever o nome correto da peça...")

    return promoverPeaoPara(peca, promocao)

def promoverPeaoPara(peao:PecaXadrez, nova_peca:str):
    match nova_peca:
        case "cavalo":
            settings.tabuleiro_principal[peao.indice_linha_atual][peao.indice_coluna_atual] = settings.peca.Cavalo(settings.jogador_atual, settings.pecas_jogadores[settings.jogador_atual][nova_peca], peao.indice_linha_atual, peao.indice_coluna_atual)
        case "torre":
            settings.tabuleiro_principal[peao.indice_linha_atual][peao.indice_coluna_atual] = settings.peca.Torre(settings.jogador_atual, settings.pecas_jogadores[settings.jogador_atual][nova_peca], peao.indice_linha_atual, peao.indice_coluna_atual)
        case "bispo":
            settings.tabuleiro_principal[peao.indice_linha_atual][peao.indice_coluna_atual] = settings.peca.Bispo(settings.jogador_atual, settings.pecas_jogadores[settings.jogador_atual][nova_peca], peao.indice_linha_atual, peao.indice_coluna_atual)
        case "rainha":
            settings.tabuleiro_principal[peao.indice_linha_atual][peao.indice_coluna_atual] = settings.peca.Rainha(settings.jogador_atual, settings.pecas_jogadores[settings.jogador_atual][nova_peca], peao.indice_linha_atual, peao.indice_coluna_atual)
    return settings.tabuleiro_principal[peao.indice_linha_atual][peao.indice_coluna_atual]
