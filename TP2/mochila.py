CONST_NOMBRE = 0
CONST_N = 1
CONST_C = 2
CONST_Z = 3
CONST_TIEMPO = 4
CONST_PRIMERA_LINEA = 5
CONST_SEPARADOR = "-----\n"
if __name__ == '__main__':
    with open('file', 'rb') as archivo:
        lineas = archivo.readlines()

    cantLineas = len(lineas)
    i = 0
    while(i < cantLineas):
        items = []
        pesoMaximo = int(lineas[CONST_C + i].split(" ")[1])
        i = i + 5
        while(lineas[i] != CONST_SEPARADOR):
            separada = lineas[i].split(",")
            valor = int(separada[1])
            peso = int(separada[2])
            id = int(separada[0])
            items.append([valor, peso,id])
            i = i + 1
        i = i + 2

