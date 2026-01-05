from settings import settings
from services.tabuleiro import tabuleiros
from models.peca_xadrez import PecaXadrez
from models.cords import Cordenadas
from services.utilitarios import impressoes

def descobrirPeca(cordenadas:Cordenadas):
    return settings.tabuleiro_principal[cordenadas.indice_linha][cordenadas.indice_coluna]

def atualizarPosicaoPeca(cordenadas:Cordenadas):
    peca = settings.tabuleiro_principal[cordenadas.indice_linha][cordenadas.indice_coluna]
    
    if peca.aparencia in settings.pecas_jogador_de_brancas or peca.aparencia in settings.pecas_jogador_de_pretas:
        peca.indice_linha_atual = cordenadas.indice_linha
        peca.indice_coluna_atual = cordenadas.indice_coluna
    
def promoverPeao(peca:PecaXadrez):
    impressoes.imprimirCabecalho("PROMOÇÃO DE PEÃO")
    tabuleiros.imprimirTabuleiro(settings.tabuleiro_principal)
    impressoes.imprimirDivisoria()
    print("Que aventura em.. deseja trocar seu peão por qual peça?\nVocê pode escolher entre 'cavalo', 'torre', 'bispo', e 'rainha'")
    
    peca = selecionarPromocaoDoPeao(peca)

    impressoes.imprimirDivisoria()
    print(f"{peca.aparencia} - Seu peão foi promovido!!")
    impressoes.imprimirDivisoria()

def selecionarPromocaoDoPeao(peca:PecaXadrez):
    promocao = "entrada inválida"
    while promocao.lower() not in ["cavalo", "torre", "bispo", "rainha"]:
        promocao = input("Resposta: ").lower()
        if promocao.lower() not in ["cavalo", "torre", "bispo", "rainha"]:
            print("! Entrada Inválida, certifique-se de escrever o nome correto da peça...")

    return promoverPeaoPara(peca, promocao)

def promoverPeaoPara(peao:PecaXadrez, nova_peca:str):
    if nova_peca == "cavalo":
        settings.tabuleiro_principal[peao.indice_linha_atual][peao.indice_coluna_atual] = settings.peca.Cavalo(settings.jogador_atual, settings.pecas_jogadores[settings.jogador_atual][nova_peca])
    elif nova_peca == "torre":
        settings.tabuleiro_principal[peao.indice_linha_atual][peao.indice_coluna_atual] = settings.peca.Torre(settings.jogador_atual, settings.pecas_jogadores[settings.jogador_atual][nova_peca])
    elif nova_peca == "bispo":
        settings.tabuleiro_principal[peao.indice_linha_atual][peao.indice_coluna_atual] = settings.peca.Bispo(settings.jogador_atual, settings.pecas_jogadores[settings.jogador_atual][nova_peca])
    elif nova_peca == "rainha":
        settings.tabuleiro_principal[peao.indice_linha_atual][peao.indice_coluna_atual] = settings.peca.Rainha(settings.jogador_atual, settings.pecas_jogadores[settings.jogador_atual][nova_peca])
    return settings.tabuleiro_principal[peao.indice_linha_atual][peao.indice_coluna_atual]
