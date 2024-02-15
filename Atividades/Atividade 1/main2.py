tabuleiro = ['0', '1', '2', '3', '4', '5', '6', '7', '8']


def imprimirTabuleiro(tabuleiro):
    print(tabuleiro[0] + ' | ' + tabuleiro[1] + ' | ' + tabuleiro[2])
    print('---------')
    print(tabuleiro[3] + ' | ' + tabuleiro[4] + ' | ' + tabuleiro[5])
    print('---------')
    print(tabuleiro[6] + ' | ' + tabuleiro[7] + ' | ' + tabuleiro[8])


def numerosCantos(tabuleiro):
    count = 0
    for i in [0, 2, 6, 8]:
        if tabuleiro[i] != 'X' and tabuleiro[i] != 'O':
            count += 1
    return count


def VerificaPosicoesVazias(tabuleiro):
    posicoesVazias = []

    for i in range(0, 9):
        if tabuleiro[i] != 'X' and tabuleiro[i] != 'O':
            posicoesVazias.append(i)
    return posicoesVazias


def verificarGanhador(tabuleiro):
    # Verificar linhas
    for i in range(0, 9, 3):
        if tabuleiro[i] == tabuleiro[i+1] == tabuleiro[i+2]:
            return tabuleiro[i]

    # Verificar colunas
    for i in range(0, 3):
        if tabuleiro[i] == tabuleiro[i+3] == tabuleiro[i+6]:
            return tabuleiro[i]

    # Verificar diagonais
    if tabuleiro[0] == tabuleiro[4] == tabuleiro[8]:
        return tabuleiro[0]
    if tabuleiro[2] == tabuleiro[4] == tabuleiro[6]:
        return tabuleiro[2]

    if all(posicao == 'X' or posicao == 'O' for posicao in tabuleiro):
        return 'Empate'

    # Caso contrário, o jogo ainda está em andamento
    return None


def movimento1(tabuleiro):
    """
    Movimento 1:
        Se o jogador começar, vá em um canto.
    """
    tabuleiro[0] = 'X'
    imprimirTabuleiro(tabuleiro)


def movimento2(tabuleiro):
    """
    Movimento 2:
        SE o outro jogador não foi lá
        ENTÃO vá no canto oposto ao movimento 1.
        SENÃO vá em um canto livre.
    """
    if tabuleiro[0] == 'X':
        if tabuleiro[8] == 'O':
            tabuleiro[6] = 'X'
        else:
            tabuleiro[8] = 'X'

    imprimirTabuleiro(tabuleiro)


def movimento3(tabuleiro):
    """
    Movimento 3:
        SE houver 2 Xs e um espaço em uma linha ENTÃO vá nesse espaço.
        SENÃO, SE houver 2 Os e um espaço em uma linha ENTÃO vá nesse espaço.
        SENÃO, SE houver 2 Os em uma coluna ENTÃO vá no meio dessa coluna.
        SENÃO vá em um canto livre.
    """

    # Verificar se há duas Xs ou duas Os em uma linha e um espaço vazio
    for linha in range(3):
        countX = 0
        countO = 0

        for j in range(3):
            i = linha * 3 + j
            if tabuleiro[i] == 'X':
                countX += 1
            if tabuleiro[i] == 'O':
                countO += 1

        if countX == 2 and countO == 0:
            for j in range(3):
                i = linha * 3 + j
                if tabuleiro[i] != 'X' and tabuleiro[i] != 'O':
                    tabuleiro[i] = 'X'
                    return
        elif countO == 2 and countX != 2:
            for j in range(3):
                i = linha * 3 + j
                if tabuleiro[i] != 'X' and tabuleiro[i] != 'O':
                    tabuleiro[i] = 'X'
                    return

    # Se não houver duas Xs ou duas Os em uma linha, verificar se há duas Os em uma coluna
    for coluna in range(3):
        countO = 0
        vazios = []

        for linha in range(3):
            i = linha * 3 + coluna
            if tabuleiro[i] == 'O':
                countO += 1
            if tabuleiro[i] != 'X' and tabuleiro[i] != 'O':
                vazios.append(i)

        if countO == 2 and len(vazios) == 1:
            tabuleiro[vazios[0]] = 'X'
            return

    # Se não houver duas Xs ou duas Os em uma linha ou duas Os em uma coluna, ir para um canto livre
    cantosVazios = numerosCantos(tabuleiro)
    if cantosVazios > 0:
        for i in [0, 2, 6, 8]:
            if tabuleiro[i] != 'X' and tabuleiro[i] != 'O':
                tabuleiro[i] = 'X'
                return


def movimento5(tabuleiro):
    """ Movimento 5: Vá no espaço livre. """
    posicoesVazias = VerificaPosicoesVazias(tabuleiro)
    tabuleiro[posicoesVazias[0]] = 'X'


def jogo(tabuleiro):
    imprimirTabuleiro(tabuleiro)
    jogador = 'X'
    movimento = 0

    while verificarGanhador(tabuleiro) is None:
        print(verificarGanhador(tabuleiro))
        if jogador == 'O':
            print("Vez do jogador O.")
            posicao = int(input("Digite uma posição de [0-8]:"))
            if tabuleiro[posicao] == 'X' or tabuleiro[posicao] == 'O':
                print("Posição ocupada. Tente novamente.")
                continue
            tabuleiro[posicao] = jogador
            jogador = 'X'
        else:
            movimento += 1
            print(f"\nComputador fez o movimento:{movimento}")
            print('-' * 50)

            if movimento == 1:
                movimento1(tabuleiro)
                jogador = 'O'
            elif movimento == 2:
                movimento2(tabuleiro)
                jogador = 'O'
            elif movimento == 3:
                movimento3(tabuleiro)
                jogador = 'O'
            elif movimento == 4:
                movimento3(tabuleiro)
                jogador = 'O'
            elif movimento == 5:
                movimento5(tabuleiro)
                jogador = 'O'
            else:
                print("Erro: Nenhum movimento disponível.")
                break
        print('-' * 50)
        imprimirTabuleiro(tabuleiro)


if __name__ == "__main__":
    jogo(tabuleiro)

    imprimirTabuleiro(tabuleiro)

    resultado = verificarGanhador(tabuleiro)
    if resultado == 'X':
        print("O jogador X venceu!")
    elif resultado == 'O':
        print("O jogador O venceu!")
    elif resultado == 'Empate':
        print("O jogo terminou em empate!")
