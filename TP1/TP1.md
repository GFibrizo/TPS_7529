# Estadístico de orden K

## Cálculo de complejidad

---

### Fuerza bruta

Se implementa un verificador que dado un conjunto y un candidato devuelve un booleano indicando si el valor indicado es el k elemento más pequeño. El algoritmo de fuerza bruta itera todos los elementos del conjunto y verifica de a uno si es la solución. Una vez el verificador devuelve true, devuelve ese elemento.

---

#### Orden de complejidad
El orden del algoritmo descripto es: **O(N * K)**, siendo N la cantidad de elementos del conjunto y K la cantidad de elementos del candidate a ser estadístico de orden K, ya que para cada

#### Ejemplos de input
Para el caso de fuerza bruta, es indiferente cual sea el conjunto, el orden de complejidad siempre es el mismo, no hay un mejor o peor caso.

---

### Ordenar y seleccionar

Ordena el conjunto mediante un algoritmo veloz de comparación y luego seleccionar el k elemento del arreglo ordenado.

#### Orden de complejidad
El orden del algoritmo utilizado depende del orden del algoritmo de ordenamiento que se use.
En el caso de la presente implementación, se utiliza la función de sort de python, el cual utiliza Timsort, que tiene una complejidad temporal de **O(N log N)**.
Por lo que el algoritmo queda acotado por esta cota. Entonces, el orden es **O(N log N)**

#### Ejemplos de input
Al depender, el orden del algoritmo, unicamente del orden del algoritmo de ordenamiento utilizado, también lo hacen los mejores y peores casos.

##### Mejor Caso
Timsort tiene por mejor caso, un orden de complejidad de **O(N)**, y se dá cuando la secuencia a ordenar ya se encuentra ordenada, debido a que busca minruns (subsecuencias de elementos ordenados dentro de la secuencia a ordenar).
  ```
  [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
  ```

---

### k-selecciones

El algoritmo de ordenamiento por selección busca el menor elemento de una secuencia y lo intercambia con el primero. Se propone realizar k selecciones para encontrar el k elemento más pequeño.

#### Orden de complejidad
El orden del algoritmo es de orden **O(N * K)** ya que se realizan K busquedas del mínimo de un segmento del conjunto.

---

### k-heapsort

Así como heapsort es una mejora del algoritmo de selección usando un heap, este algoritmo mejora el de k-selecciones haciendo k extracciones a un arreglo con la propiedad de heap.

#### Orden de complejidad
El orden del algoritmo es **O(K log N)**, ya que, si bien el heapify es de orden O(N), queda acotado el tiempo que insumen las K iteraciones en las cuales, en cada una realiza un pop del heap, operación que tarda log N (siendo N la cantidad de elementos del heap).

#### Ejemplos de input
El algoritmo k-heapsort depende directamente del orden de heapify (función para transformar una secuencia en un heap). Por ende, y como heapify no tiene mejor o peor caso, tampoco lo tiene k-heapsort.

---

### HeapSelect

Se propone usar un heap para almacenar los k elementos más chicos, intercambiándolos cuando sea necesario.

#### Orden de complejidad
El orden del algorimo es **O(N log K)**, ya que se recorren todos los elementos del conjunto, y por cada iteración se realiza un push al heap y a veces un pop, que son operaciones de tiempo O(log K) siendo log K la altura del heap. 

#### Ejemplos de input

##### Mejor Caso
```
[15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
  ```
##### Peor Caso
```
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
  ```

---

### QuickSelect

Se usa una estrategia de división y conquista similar a la de quicksort pero descartando las divisiones que sabemos que no incluyen al k buscado.

#### Orden de complejidad
El orden del algoritmo es **O(N)**, ya que basta con recorrer una vez el conjunto para encontrar los menores al candidato, y otra vez para contar dicha cantidad (se puede optimizar, conservando el orden, pero recorriendo el conjunto 1 sola vez, contando la cantidad de elementos a la vez que se los clasifica).
