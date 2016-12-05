from math import ceil


def round(valor, n, max_value, precision):
    result = int(ceil(valor / (max_value * (precision / n))))
    return result

def calcular_mochila(items, pesoMax, precision):
    n = len(items)
    filtered_items = filter(lambda item: (item[1] <= pesoMax), items)
    max_value = reduce(lambda item1, item2: item1 if item1[0] > item2[0] else item2, filtered_items)[0]
    filtered_items = map(lambda item: [round(item[0], n, max_value, precision), item[1], item[2]], filtered_items)
    resultado1, resultado2 = _calcular_mochila3(filtered_items, pesoMax)
    return reduce(lambda valor1, valor2:  valor1 + valor2, [items[i][0] for i in resultado2]), map(lambda index: items[index], resultado2) 


def round1(valor, n, max_value, precision):
    result = int(ceil(valor / (max_value * (precision / (2 * n)))))
    return result

def calcular_mochil(items, pesoMax, precision):
    n = len(items)
    filtered_items = filter(lambda item: (item[1] <= pesoMax), items)
    data = map(lambda item: item[0], filtered_items[:100])
    max_value = reduce(lambda item1, item2: item1 if item1[0] > item2[0] else item2, filtered_items)[0]
    filtered_items = map(lambda item: [round1(item[0], n, max_value, precision), item[1], item[2]], filtered_items)
    resultado1, resultado2 = _calcular_mochila2(filtered_items, pesoMax)

    print resultado2
    #print reduce(lambda item1, item2:  item1 + item2, data)
    return resultado1 * max_value, map(lambda x: x * max_value, resultado2) 







def _calcular_mochila(items, pesoMax):
    matrizDevolucion = []
    valores = [[0] * (pesoMax + 1)
    for i in xrange(len(items) + 1)]
    for i, (valor, peso, id) in enumerate(items):
        i += 1
        for capacidad in xrange(pesoMax + 1):
            if peso > capacidad:
                valores[i][capacidad] = valores[i - 1][capacidad]
            else:
                primerCandidato = valores[i - 1][capacidad]
                segundoCandidato = valores[i - 1][capacidad - peso] + valor
                valores[i][capacidad] = max(primerCandidato, segundoCandidato)
    longItems = len(items)
    j = pesoMax
    while longItems > 0:
        if valores[longItems][j] != valores[longItems - 1][j]:
            matrizDevolucion.append(items[longItems - 1])
            j -= items[longItems - 1][1]
        longItems -= 1
    matrizDevolucion.reverse()
    return valores[len(items)][pesoMax], matrizDevolucion






def _calcular_mochila2(items, pesoMax):
    sumVal = sum_valores_hasta(items, len(items))
    #print sumVal
    M = [[float("inf")]*sumVal]*len(items)

    for i in xrange(len(items)):
        M[i][0] = 0

    for i in xrange(1, len(items)):
        sum_valores = sum_valores_hasta(items, i)
        for valor in xrange(1, sum_valores):
            if valor > sum_valores_hasta(items, i-1):
                M[i][valor] =  items[i][1] + M[i-1][max(0, valor - items[i][0])] #items[i][1] + M[i-1][valorMax] #
            else:
                M[i][valor] = min(M[i-1][valor], items[i][1] + M[i-1][max(0, valor - items[i][0])])
    valorMax = getValorMaxEnM(M, pesoMax, items)
    print M[len(items)-1][valorMax], "<=", pesoMax
    return valorMax, getConjuntoSolucion(M, valorMax, items)




def sum_valores_hasta(items, pos):
    total = 0
    for i in xrange(pos):
        #print items[i][0]
        total += items[i][0]
    return total



def getValorMaxEnM(M, pesoMax, items):
    valorMax = 0
    n = len(items)-1
    for valor in xrange(len(M[n])):  
        if M[n][valor] <= pesoMax and valor >= valorMax:
            valorMax = valor
    return valorMax




def _calcular_mochila3(items, pesoMax):
    sumVal = sum_valores_hasta(items, len(items))
    n = len(items)
    M = [[0]*sumVal]*len(items)
    #print sumVal

    for i in xrange(1, sumVal):
        M[0][i] = float("inf")

    for i in xrange(1, n):
        for valor in xrange(1, sumVal):
            if items[i][0] <= valor:
                M[i][valor] = min(M[i-1][valor], items[i][1] + M[i-1][valor - items[i][0]])
            else:
                M[i][valor] = M[i-1][valor]                
    valorMax = getValorMaxEnM(M, pesoMax, items)

    #raw_input()    
    #print valorMax, "<<=", pesoMax
    return valorMax, getConjuntoSolucion(M, valorMax, items)





def getConjuntoSolucion(M, valorMax, items):
    solucion = []
    valor = valorMax
    for i in xrange(len(items)-1, 0, -1):
        if (items[i][0]) <= valor:
            #print "get conjunto solucion"
            #print items[i][1] + M[i-1][valor - items[i][0]]
            #print M[i-1][valor]
            #raw_input()
            
            if (items[i][1] + M[i-1][valor - items[i][0]]) <= M[i-1][valor]:
                solucion.append(i)
                valor -= items[i][0]
    return solucion