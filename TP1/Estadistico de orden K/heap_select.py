import heapq

class MaxHeap(object):
    def __init__(self, x):
        self.heap = [-e for e in x]
        heapq.heapify(self.heap)
    def push(self, value):
        heapq.heappush(self.heap, -value)
    def pop(self):
        return -heapq.heappop(self.heap)
    def __len__(self):
        return len(self.heap)


def es_estadistico_orden_k(conjunto, candidato, k):

    heap = MaxHeap([])
    elemento = 0
    for elem in conjunto:
        heap.push(elem)
        if (len(heap) > k):
            elemento = heap.pop()
            break

    print "Candidato: " + str(candidato) + "\tEstadistico de orden" + str(k) + ": " + str(elemento)
    return candidato == elemento

################################################################################
################################################################################

def test():
    print es_estadistico_orden_k([1], 1, 0)
    print es_estadistico_orden_k([2,1], 2, 1)
    print es_estadistico_orden_k([3,1,4,2,7], 4, 3)
    print es_estadistico_orden_k([1,2,3,4,5,6,7,8], 1, 0)
    print es_estadistico_orden_k([1,2,3,4,5,6,7,8], 8, 7)
    print es_estadistico_orden_k([1,2,3,4,5,6,7,8], 5, 4)

################################################################################
################################################################################

test()
