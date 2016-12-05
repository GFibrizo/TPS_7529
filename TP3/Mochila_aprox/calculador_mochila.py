from math import ceil


def round(valor, n, max_value, precision):
    result = int(ceil(valor / (max_value * (precision / n))))
    return result


def calcular_mochila(items, pesoMax, precision):
    n = len(items)
    filtered_items = filter(lambda item: (item[1] <= pesoMax), items)
    max_value = reduce(lambda item1, item2: item1 if item1[0] > item2[0] else item2, filtered_items)[0]
    filtered_items = map(lambda item: [round(item[0], n, max_value, precision), item[1], item[2]], filtered_items)
    resultado1, resultado2 = _calcular_mochila(filtered_items, pesoMax)
    return reduce(lambda valor1, valor2:  valor1 + valor2, [items[i][0] for i in resultado2]), resultado2 


def sum_valores_hasta(items, pos):
    total = 0
    for i in xrange(pos):
        total += items[i][0]
    return total


def getValorMaxEnM(M, pesoMax, items):
    valorMax = 0
    n = len(items)-1
    for valor in xrange(len(M[n])):  
        if M[n][valor] <= pesoMax and valor >= valorMax:
            valorMax = valor
    return valorMax


def _calcular_mochila(items, pesoMax):
    sumVal = sum_valores_hasta(items, len(items))
    n = len(items)
    M = [[0]*sumVal]*len(items)

    for i in xrange(1, sumVal):
        M[0][i] = float("inf")

    for i in xrange(1, n):
        for valor in xrange(1, sumVal):
            if items[i][0] <= valor:
                M[i][valor] = min(M[i-1][valor], items[i][1] + M[i-1][valor - items[i][0]])
            else:
                M[i][valor] = M[i-1][valor]                
    valorMax = getValorMaxEnM(M, pesoMax, items)
    return valorMax, getConjuntoSolucion(M, valorMax, items)


def getConjuntoSolucion(M, valorMax, items):
    solucion = []
    valor = valorMax
    for i in xrange(len(items)-1, 0, -1):
        if (items[i][0]) <= valor:            
            if (items[i][1] + M[i-1][valor - items[i][0]]) <= M[i-1][valor]:
                solucion.append(i)
                valor -= items[i][0]
    return solucion
