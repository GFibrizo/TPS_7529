import csv
import sys

import calculador_mochila
import time

CONST_NOMBRE = 0
CONST_N = 1
CONST_C = 2
CONST_Z = 3
CONST_TIEMPO = 4
CONST_PRIMERA_LINEA = 5
CONST_ID = 0
CONST_VALOR = 1
CONST_PESO = 2
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
            tiempoTotalPisinger = float(lineas[CONST_TIEMPO + i].split(" ")[1])
            valorMaxPisinger = int(lineas[CONST_Z + i].split(" ")[1])
            i = i + 5
            while(lineas[i] != CONST_SEPARADOR):
                separada = lineas[i].split(",")
                id = int(separada[CONST_ID])
                valor = int(separada[CONST_VALOR])
                peso = int(separada[CONST_PESO])
                items.append([valor, peso, id])
                i = i + 1
            inicio = time.time()
            mejorValorAlgoritmo, objetos = calculador_mochila.calcular_mochila(items, pesoMaximo)
            tiempoAlgoritmo = time.time() - inicio
            spamwriter.writerow(["Listado numero {0}, peso maximo: {1}".format(listado, pesoMaximo)])
            for valor, peso, id in objetos:
                 spamwriter.writerow(["Id:{2}, Valor: {0}, Peso: {1}".format(valor, peso, id)])
            i = i + 2
            spamwriter.writerow(["-------"])




