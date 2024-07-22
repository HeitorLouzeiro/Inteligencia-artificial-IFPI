from matplotlib import pyplot as plt

from AGgenetico import evolve, media_fitness, populacao

pesoValores = [(4, 30), (8, 10), (8, 30), (25, 75), (2, 10),
               (50, 100), (6, 300), (12, 50), (100, 400), (8, 300)]


pesoMaximo = 150
numeroItens = len(pesoValores)
numeroCromossomos = 100
geracoes = 100
probabilidadeMutacao = 0.05

# Execução dos procedimentos
populacao_atual = populacao(numeroCromossomos, numeroItens)
historico_de_fitness = [media_fitness(
    populacao_atual, pesoMaximo, pesoValores)]
for i in range(geracoes):
    populacao_atual = evolve(populacao_atual, pesoMaximo,
                             pesoValores, numeroCromossomos, probabilidadeMutacao)
    historico_de_fitness.append(media_fitness(
        populacao_atual, pesoMaximo, pesoValores))

# Prints do terminal
for indice, dados in enumerate(historico_de_fitness):
    print("Geracao: ", indice, " | Media de valor na mochila: ", dados)

print("\nPeso máximo:", pesoMaximo, "g\n\nItens disponíveis:")
for indice, item in enumerate(pesoValores):
    print("Item ", indice + 1, ": ", item[0], "g | R$", item[1])

print("\nExemplos de boas solucoes: ")
for i in range(5):
    print(populacao_atual[i])

# Gerador de gráfico

plt.plot(range(len(historico_de_fitness)), historico_de_fitness)
plt.grid(True, zorder=0)
plt.title("Problema da mochila")
plt.xlabel("Geracao")
plt.ylabel("Valor medio da mochila")
plt.show()
