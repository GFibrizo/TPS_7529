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

################################################################################
################################################################################

def obtener_estadistico_orden_k(conjunto, k):
    heap = MaxHeap([])
    elemento = 0
    for elem in conjunto:
        heap.push(elem)
        if (len(heap) > k):
            elemento = heap.pop()
            break
    return elemento

################################################################################
################################################################################

def test():
    print obtener_estadistico_orden_k([1], 0) == 1
    print obtener_estadistico_orden_k([2,1], 1) == 2
    print obtener_estadistico_orden_k([3,1,4,2,7], 3) == 4
    print obtener_estadistico_orden_k([1,2,3,4,5,6,7,8], 0) == 1
    print obtener_estadistico_orden_k([1,2,3,4,5,6,7,8], 7) == 8
    print obtener_estadistico_orden_k([1,2,3,4,5,6,7,8], 4) == 5

################################################################################
################################################################################

test()
