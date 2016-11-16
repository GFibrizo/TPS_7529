def calcular_mochila(items, pesoMax):
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