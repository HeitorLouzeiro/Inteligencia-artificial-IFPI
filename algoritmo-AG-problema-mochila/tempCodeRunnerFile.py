from matplotlib import pyplot as plt

from AGgenetico import evolve, media_fitness, populacao

pesoValores = [(2, 3), (3, 4), (4, 5), (5, 8), (9, 10),
               (6, 8), (7, 10), (8, 11), (10, 13), (11, 15)]

pesoMaximo = 20
numeroItens = len(pesoValores)
numeroCromossomos = 100
geracoes = 100
probabilidadeMutacao = 0.1

# EXECUCAO DOS PROCEDIMENTOS
populacao = populacao(numeroCromossomos, numeroItens)
historico_de_fitness = [media_fitness(populacao, pesoMaximo, pesoValores)]
for i in range(geracoes):
    populacao = evolve(populacao, pesoMaximo,
                       pesoMaximo, numeroCromossomos)
    historico_de_fitness.append(media_fitness(
        populacao, pesoMaximo, pesoMaximo))

# PRINTS DO TERMINAL
for indice, dados in enumerate(historico_de_fitness):
    print("Geracao: ", indice, " | Media de valor na mochila: ", dados)

print("\nPeso máximo:", pesoMaximo, "g\n\nItens disponíveis:")
for indice, i in enumerate(pesoMaximo):
    print("Item ", indice+1, ": ", i[0], "g | R$", i[1])

print("\nExemplos de boas solucoes: ")
for i in range(5):
    print(populacao[i])

# GERADOR DE GRAFICO

plt.plot(range(len(historico_de_fitness)), historico_de_fitness)
plt.grid(True, zorder=0)
plt.title("Problema da mochila")
plt.xlabel("Geracao")
plt.ylabel("Valor medio da mochila")
plt.show()
plt.show()
plt.show()
