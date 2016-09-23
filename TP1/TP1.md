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

El orden del algoritmo es de orden O(N * K) ya que se realizan K busquedas del mínimo de un segmento del conjunto.

### k-heapsort

Así como heapsort es una mejora del algoritmo de selección usando un heap, este algoritmo mejora el de k-selecciones haciendo k extracciones a un arreglo con la propiedad de heap.

El orden del algoritmo es O(K log N), ya que, si bien el heapify es de orden O(N), queda acotado el tiempo que insumen las K iteraciones en las cuales, en cada una realiza un pop del heap, operación que tarda log N (siendo N la cantidad de elementos del heap).

### HeapSelect

Se propone usar un heap para almacenar los k elementos más chicos, intercambiándolos cuando sea necesario.

El orden del algorimo es O(N log K), ya que se recorren todos los elementos del conjunto, y por cada iteración se realiza un push al heap y a veces un pop, que son operaciones de tiempo O(log K) siendo log K la altura del heap. 

### QuickSelect

Se usa una estrategia de división y conquista similar a la de quicksort pero descartando las divisiones que sabemos que no incluyen al k buscado.

El orden del algoritmo es O(N), ya que basta con recorrer una vez el conjunto para encontrar los menores al candidato, y otra vez para contar dicha cantidad (se puede optimizar, conservando el orden, pero recorriendo el conjunto 1 sola vez, contando la cantidad de elementos a la vez que se los clasifica).
