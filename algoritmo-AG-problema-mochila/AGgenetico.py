from random import choice, randint, random


def individuo(nItens):
    return [choice([0, 1]) for i in range(nItens)]


def populacao(nIndividuos, nItens):
    return [individuo(nItens) for i in range(nIndividuos)]


def fitness(individuo, pesoMaximo, pesoValores):
    pesoTotal = 0
    valorTotal = 0

    for index, valor in enumerate(individuo):
        if valor == 1:
            pesoTotal += pesoValores[index][0]
            valorTotal += pesoValores[index][1]

    if pesoMaximo - pesoTotal < 0:
        return -1

    return valorTotal


def media_fitness(populacao, pesoMaximo, pesoValores):
    soma = sum(fitness(x, pesoMaximo, pesoValores)
               for x in populacao if fitness(x, pesoMaximo, pesoValores) >= 0)
    return soma / (len(populacao) * 1.0)


def sortearRoleta(pais, fitnessTotal, indexIgnorar=-1):
    roleta, acumulado, valor_sorteado = [], 0, random()

    for indice, i in enumerate(pais):
        if indexIgnorar == indice:
            continue
        acumulado += i[0]
        roleta.append(acumulado / fitnessTotal)
        if roleta[-1] >= valor_sorteado:
            return indice

    return len(pais) - 1  # Caso não encontre, retorna o último índice


def evolve(populacao, pesoMaximo, pesoValores, numeroCromossomos, mutacao=0.05):
    pais = [[fitness(x, pesoMaximo, pesoValores), x]
            for x in populacao if fitness(x, pesoMaximo, pesoValores) >= 0]
    pais.sort(reverse=True, key=lambda x: x[0])

    fitnessTotal = sum(x[0] for x in pais)

    # REPRODUCAO
    filhos = []
    while len(filhos) < numeroCromossomos:
        indice_pai = sortearRoleta(pais, fitnessTotal)
        indice_mae = sortearRoleta(pais, fitnessTotal, indice_pai)

        pai = pais[indice_pai][1]
        mae = pais[indice_mae][1]

        meio = len(pai) // 2
        filho = pai[:meio] + mae[meio:]
        filhos.append(filho)

    # MUTACAO
    for individuo in filhos:
        if mutacao > random():
            pos_to_mutacao = randint(0, len(individuo) - 1)
            individuo[pos_to_mutacao] = 1 if individuo[pos_to_mutacao] == 0 else 0

    return filhos
