# Estadístico de orden K

## Cálculo de complejidad


### Fuerza bruta

Se implementa un verificador que dado un conjunto y un candidato devuelve un booleano indicando si el valor indicado es el k elemento más pequeño. El algoritmo de fuerza bruta itera todos los elementos del conjunto y verifica de a uno si es la solución. Una vez el verificador devuelve true, devuelve ese elemento.

El orden del algoritmo descripto es: O(N * K)
Siendo N la cantidad de elementos del conjunto y K la cantidad de elementos del candidate a ser estadístico de orden K.

### Ordenar y seleccionar

Ordena el conjunto mediante un algoritmo veloz de comparación y luego seleccionar el k elemento del arreglo ordenado.

El orden del algoritmo utilizado depende del orden del algoritmo de ordenamiento que se use.
Se utiliza la función de sort de python, el cual utiliza Timsort, que tiene una complejidad temporal de O(N log N).
Por lo que el algoritmo queda acotado por esta cota. Entonces, el orden es O(N log N)


### k-selecciones

El algoritmo de ordenamiento por selección busca el menor elemento de una secuencia y lo intercambia con el primero. Se propone realizar k selecciones para encontrar el k elemento más pequeño.

### k-heapsort


### HeapSelect


### QuickSelect
