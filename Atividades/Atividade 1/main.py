# Função para imprimir o tabuleiro

import random

tabuleiro = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Cantos do tabuleiro: 1, 3, 7, 9
# Meio do tabuleiro: 2,5,8
# Laterais do tabuleiro: 4,6

jogador = 0
Vitoria = True


def imprimirTabuleiro(tabuleiro):
    print("\nImprimindo o tabuleiro")
    print(tabuleiro[0], "|", tabuleiro[1], "|", tabuleiro[2])
    print("-"*10)
    print(tabuleiro[3], "|", tabuleiro[4], "|", tabuleiro[5])
    print("-"*10)
    print(tabuleiro[6], "|", tabuleiro[7], "|", tabuleiro[8])
    print("\n")


def movimento2(tabuleiro):
    """
    Movimento 2:
    SE o outro jogador não foi lá
    ENTÃO vá no canto oposto ao movimento 1.
    SENÃO vá em um canto livre.
    """
    while True:
        # Se o outro jogador não foi lá
        if tabuleiro[0] == 'X':
            if tabuleiro[8] == '0':
                tabuleiro[random.choice([2, 6])] = 'X'
            else:
                tabuleiro[8] = 'X'
        elif tabuleiro[2] == 'X':
            if tabuleiro[6] == '0':
                tabuleiro[random.choice([0, 8])] = 'X'
            else:
                tabuleiro[6] = 'X'
        elif tabuleiro[6] == 'X':
            if tabuleiro[2] == '0':
                tabuleiro[random.choice([0, 8])] = 'X'
            else:
                tabuleiro[2] = 'X'
        elif tabuleiro[8] == 'X':
            if tabuleiro[0] == '0':
                tabuleiro[random.choice([2, 6])] = 'X'
            else:
                tabuleiro[0] = 'X'
        break


def movimento3(tabuleiro):
    """
    Movimento 3:
    SE houver 2 Xs e um espaço em uma linha
    ENTÃO vá nesse espaço.
    SENÃO, SE houver 2 Os e um espaço em uma linha
    ENTÃO vá nesse espaço.
    SENÃO vá em um canto livre.
    """
    global Vitoria
    print("Movimento 3")
    # Verificar se há 2 Xs e um espaço em uma linha
    while True:
        # Verifcar se há 2 Xs e um espaço em uma linha
        if tabuleiro[0] == 'X' and tabuleiro[8] == 'X':
            # Se houver 2 Xs e um espaço em uma linha
            if tabuleiro[4] != '0':
                tabuleiro[4] = 'X'
                imprimirTabuleiro(tabuleiro)
                print("Computador venceu!")
                Vitoria = False
                return Vitoria
            # Verificar se o espaço com o numero 3 está livre
            elif tabuleiro[6] == '0' and tabuleiro[4] == '0':
                tabuleiro[2] = 'X'
                return Vitoria
            # Verificar se o espaço com o numero 7 está livre
            elif tabuleiro[2] == '0' and tabuleiro[4] == '0':
                tabuleiro[6] = 'X'
                return Vitoria
            elif tabuleiro[1] == '0' and tabuleiro[4] == '0':
                tabuleiro[7] = 'X'
            else:
                while [3, 4, 5]:
                    if tabuleiro[3] != '0':
                        tabuleiro[3] = 'X'
                        break
                    elif tabuleiro[4] != '0':
                        tabuleiro[4] = 'X'
                        break
                    elif tabuleiro[5] != '0':
                        tabuleiro[5] = 'X'
                        break
                    break
        break


def movimento4(tabuleiro):
    """
    Movimento 4:
    SE houver 2 Xs e um espaço em uma linha
    ENTÃO vá nesse espaço.
    SENÃO, SE houver 2 Os e um espaço em uma linha
    ENTÃO vá nesse espaço.
    SENÃO vá em um canto livre.
    """
    global Vitoria
    print("Movimento 4")
    # Verificar se há 2 Xs e um espaço em uma linha
    """     posicoesVazias = []

        for i in range(0, 9):
            if tabuleiro[i] == i+1:
                posicoesVazias.append(i)

        print(posicoesVazias)
    """
    while True:
        if ((tabuleiro[0] == 'X' and tabuleiro[8] == 'X') and
                (tabuleiro[0] == 'X' and tabuleiro[6] == 'X')):
            if tabuleiro[3] != '0':
                tabuleiro[3] = 'X'
                imprimirTabuleiro(tabuleiro)
                print("Computador venceu!")
                Vitoria = False
                return Vitoria
            else:
                tabuleiro[7] = 'X'
                imprimirTabuleiro(tabuleiro)
                print("Computador venceu!")
                Vitoria = False
                return Vitoria
        elif ((tabuleiro[0] == 'X' and tabuleiro[2] == 'X') and
                (tabuleiro[2] == 'X' and tabuleiro[8] == 'X')):
            if tabuleiro[1] != '0':
                print("Entrou aqui")
                tabuleiro[1] = 'X'
                imprimirTabuleiro(tabuleiro)
                print("Computador venceu!!")
                Vitoria = False
                return Vitoria
            else:
                print("Entrou aqui no else1")
                tabuleiro[5] = 'X'
                imprimirTabuleiro(tabuleiro)
                print("Computador venceu!")
                Vitoria = False
                return Vitoria
        else:
            movimento3(tabuleiro)
            print("Entrou no else")


def jogo(tabuleiro):
    jogador = '0'

    """
    Movimento 1: Vá em um canto.
    Colocando X em um canto aleatório do tabuleiro
    """
    # tabuleiro[random.choice([0, 2, 6, 8])] = 'X'
    tabuleiro[0] = 'X'
    movimentoAtual = 1

    while Vitoria is True:

        imprimirTabuleiro(tabuleiro)
        print(f"Turno do jogador {jogador}")

        if jogador == '0':
            jogada = int(
                input("Selecione um número de  1 a  9 para jogar: ")) - 1
            if tabuleiro[jogada] != 'X' and tabuleiro[jogada] != '0':
                tabuleiro[jogada] = jogador
                jogador = 'X'
            else:
                print("Posição já ocupada. Tente novamente.")

        else:
            movimentoAtual += 1

            if movimentoAtual == 2:
                movimento2(tabuleiro)
            elif movimentoAtual == 3:
                movimento3(tabuleiro)
            elif movimentoAtual == 4:
                movimento4(tabuleiro)

            jogador = '0'

        print(movimentoAtual)


def menu():
    imprimirTabuleiro(tabuleiro)
    print("-"*20)
    jogo(tabuleiro)


menu()
