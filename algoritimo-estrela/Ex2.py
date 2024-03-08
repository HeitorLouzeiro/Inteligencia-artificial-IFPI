from pyamaze import agent, maze


def h_score():
    pass


def estrela(labirinto):
    # criar o tabuleiro com todo mundo com f_score infinito
    # calcular o valor da celula inicial
    # caminhar a partir da celula inicial explorando os proximos caminhos
    # para cada possibilidade de caminho
    # se o caminho é possivel (não tem parede)
    # calcular o f_score dos caminhos possiveis
    # se o f_score calculado < f_score antigo do caminho
    # substituir o f_score antigo pelo calculado
    # escolher o caminho para seguir que tem:
    # o menor f_score
    # se os f_score forem iguais, o que tem menor h_score
    """
        N - Norte
        S - Sul
        W - Oeste
        E - Leste
    """
    # O caminho vai ser representado assim.
    # caminho = {(10, 10): (10, 9), (10, 9): (9, 9), (9, 9): (9, 8)}
    caminho = "NNWWWNNWWW"
    return caminho


# Criação do laberinto.
labirinto = maze()
labirinto.CreateMaze()

# Agente que vai camainhar o laberinto
agente = agent(labirinto, filled=True, footprints=True)

caminho = estrela(labirinto)

# Mostrar o caminha que ele vai fazer.
labirinto.tracePath({agente: caminho}, delay=300)

labirinto.run()
