from services.utilitarios import iniciar_partida

entrada = "entrada invalida"
while True:
    entrada = input("Digite o número da ação que deseja\n1. Jogar partida de xadrez\n2. Sair do jogo\nResposta: ")
    if entrada not in ["1","2"]:
        print("Entrada Inválida, digite 1 ou 2.")
        continue
    match entrada:
        case "1":
            iniciar_partida.iniciarPartida()
        case "2":
            print("Obrigado por jogar! ;)")
            break