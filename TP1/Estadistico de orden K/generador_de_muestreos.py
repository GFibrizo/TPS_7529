import random
import fuerza_bruta
import heap_select
import k_heapsort
import k_selecciones
import quick_select
import ordenar_y_seleccionar
import os.path
import time
import csv

CANT_ITERACIONES = 40

funcdict = {
    'fuerza_bruta.obtener_estadistico_orden_k': fuerza_bruta.obtener_estadistico_orden_k,
    'heap_select.obtener_estadistico_orden_k': heap_select.obtener_estadistico_orden_k,
    'k_heapsort.obtener_estadistico_orden_k': k_heapsort.obtener_estadistico_orden_k,
    'k_selecciones.obtener_estadistico_orden_k': k_selecciones.obtener_estadistico_orden_k,
    'quick_select.obtener_estadistico_orden_k': quick_select.obtener_estadistico_orden_k,
    'ordenar_y_seleccionar.obtener_estadistico_orden_k': ordenar_y_seleccionar.obtener_estadistico_orden_k,
}

func3params = {
    'fuerza_bruta.obtener_estadistico_orden_k'
}

def generar_muestra(cantidad):
    return [random.randint(1,10) for i in range(cantidad)]

def tomar_muestreos():
    fname = obtener_nuevo_archivo()
    with open(fname, 'w') as csvfile:
        spamwriter = csv.writer(csvfile)
        # Headers
        spamwriter.writerow(['Algoritmo', 'Tamano', 'Tiempo del algoritmo', 'Candidato', 'K', 'Resultado'])
        # Distintos tamanos
        for N in obtener_tamanos():
            muestra = generar_muestra(N)
            candidato = random.randint(0,10)
            k = random.randint(0,N-1)
            # Se verifica el tiempo en cada estadistico
            for func in funcdict:
                tiempo_algoritmo_promedio = 0
                for i in range(0, CANT_ITERACIONES):
                    inicio = time.time()
                    resultado = funcdict[func](muestra, candidato)
                    tiempo_algoritmo_promedio = tiempo_algoritmo_promedio + (time.time() - inicio)
                spamwriter.writerow([func, N, tiempo_algoritmo_promedio / CANT_ITERACIONES,candidato,k,resultado])


def obtener_tamanos():
    return [25,50,75,100,200]

def obtener_nuevo_archivo():
    it = 0
    name = "../Tiempos/tiempos"
    extension = ".csv"
    while(True):
        fname = name + str(it) + extension
        if not os.path.isfile(fname):
            return fname
        it = it + 1
        if it > 100:
            return "../Tiempos/tiempos101.csv"




tomar_muestreos()