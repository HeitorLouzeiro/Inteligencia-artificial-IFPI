# Quantiade de solucoes encontradas
solucoes = 0
# Funcao que imprime o tabuleiro

# Mostre o tabuleiro


def mostrar_tabuleiro(tab, N):
    """
    Criando um tabuleiro
    i = linha
    j = coluna
    """
    for i in range(N):
        for j in range(N):
            # Se a posição for 1, imprima R
            if tab[i][j] == 1:
                print("R\t", end="")
            # Se não, imprima -
            else:
                print("-\t", end="")
        print("\n\n")
    print("\n")


def posicaoSegura(tab, N, lin, col):
    """
    Verifica se é seguro colocar a rainha numa determinada coluna
    """
    # verifica se ocorre ataque na linha
    for i in range(N):
        """
        Se a posição for 1, retorne falso, ou seja não é seguro
        Se tiver uma rainha na linha, retorne falso
        Exemplo:

        tab[1][1] == 1

        R R - -
        - - - -
        - - - -
        - - - -

        """
        if tab[lin][i] == 1:
            return False

    # verifica se ocorre ataque na coluna
    for i in range(N):
        """
        Se a posição for 1, retorne falso, ou seja não é seguro
        Se tiver uma rainha na coluna, retorne falso
        Exemplo:
        tab[0][1] == 1
        R - - -
        R - - -
        - - - -
        - - - -
        """
        if tab[i][col] == 1:
            return False

    """
        verifica se ocorre ataque na diagonal principal de cima para baixo
        da esquerda para a direita

        tab[2][2] == 1
        i = 2
        j = 2
    """

    i = lin
    j = col
    while i >= 0 and j >= 0:
        """
            tab[1][1] == 1
            R - - -         R - - -
            - - - -         - - - -
            - - R -         - R - -
            - - - -         - - - -
        """
        if tab[i][j] == 1:
            return False
        # Diminui a linha e a coluna i = 1, j = 1
        i -= 1
        j -= 1

    """
    Aumenta a linha e a coluna
    i = 2
    j = 2
    """
    i = lin
    j = col
    while i < N and j < N:
        """
            tab[2][2] == 1
            R - - -      R - - -
            - - - -      - - - -
            - - R -      - - - R
            - - - -      - - - -
        """
        if tab[i][j] == 1:
            return False

        # Aumenta a linha e a coluna i = 3, j = 3
        i += 1
        j += 1

    """
    Verifica se ocorre ataque na diagonal secundária acima e abaixo
    da esquerda para a direita
    """
    i = lin
    j = col

    while i >= 0 and j < N:
        """
            tab[2][2] == 1
            R - - -      R - - -
            - - - -      - - - R
            - - R -      - - - -
            - - - -      - - - -
        """

        if tab[i][j] == 1:
            return False
        # Diminui a linha e aumenta a coluna i = 1, j = 3
        i -= 1
        j += 1

    """
    Verifica se ocorre ataque na diagonal secundária acima e abaixo
    da direita para a esquerda
    """
    i = lin
    j = col

    while i < N and j >= 0:
        """
            tab[2][2] == 1
            R - - -      R - - -
            - - - -      - - - -
            - - R -      - - - -
            - - - -      - R - -
        """
        if tab[i][j] == 1:
            return False
        # Aumenta a linha e diminui a coluna i = 3, j = 1
        i += 1
        j -= 1

    # se chegou aqui, então está seguro (retorna True)
    return True


def criaSolucao(tab, N, col):
    # solucoes é uma variável global para contar o número de soluções
    global solucoes

    # se todas as rainhas estiverem colocadas, imprime o tabuleiro
    if col == N:
        print(f"Solução {solucoes + 1}:")
        mostrar_tabuleiro(tab, N)
        solucoes += 1
        return

    # para cada linha, tenta colocar a rainha
    for i in range(N):
        # se a posição for segura, coloca a rainha
        """
        Se a posição for segura, coloque a rainha
        tab = tabuleiro
        N = número de rainhas
        i = linha
        col = coluna
        """
        if posicaoSegura(tab, N, i, col):
            # coloca a rainha
            tab[i][col] = 1
            # chama recursivamente para a próxima coluna
            criaSolucao(tab, N, col + 1)
            # se não encontrar solução, remove a rainha
            tab[i][col] = 0


def main():
    N = int(input("Digite o número de rainhas: "))
    tab = [[0] * N for _ in range(N)]

    print("Tabuleiro inicial:")
    mostrar_tabuleiro(tab, N)

    """
    Imprime todas as soluções encontradas
    tab = tabuleiro
    N = número de rainhas
    col = 0 (coluna inicial)
    """
    criaSolucao(tab, N, 0)
    print(f"Total de soluções encontradas: {solucoes}")


if __name__ == "__main__":
    main()
