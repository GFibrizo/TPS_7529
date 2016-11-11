import csv
import sys

import calculador_mochila

CONST_NOMBRE = 0
CONST_N = 1
CONST_C = 2
CONST_Z = 3
CONST_TIEMPO = 4
CONST_PRIMERA_LINEA = 5
CONST_SEPARADOR = "-----\n"
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('parametro 1: archivo de entrada, parametro 2: archivo de salida')
        sys.exit()
    archivoEntrada = sys.argv[1]
    archivoSalida = sys.argv[2]
    with open(archivoSalida, 'w') as csvfile:
        spamwriter = csv.writer(csvfile)
        with open(archivoEntrada, 'rb') as archivo:
                lineas = archivo.readlines()
        cantLineas = len(lineas)
        i = 0
        listado = 0
        while(i < cantLineas):
            listado = listado + 1
            items = []
            pesoMaximo = int(lineas[CONST_C + i].split(" ")[1])
            i = i + 5
            while(lineas[i] != CONST_SEPARADOR):
                separada = lineas[i].split(",")
                id = int(separada[0])
                valor = int(separada[1])
                peso = int(separada[2])
                items.append([valor, peso, id])
                i = i + 1
            mejorValor, objetos = calculador_mochila.calcular_mochila(items, pesoMaximo)
            spamwriter.writerow(["Mejor valor para listado numero {0}: {1} y peso maximo: {2}".format(listado, mejorValor, pesoMaximo)])
            for valor, peso, id in objetos:
                 spamwriter.writerow(["Id:{2}, Valor: {0}, Peso: {1}".format(valor, peso, id)])
            i = i + 2
            spamwriter.writerow(["-------"])




