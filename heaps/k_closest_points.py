import math

from heaps.heap import MinHeap


def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    heap = MinHeap([[math.sqrt(x**2 + y**2), x, y] for x, y in points], limit=k)
    print(heap)
    result = []
    while heap:
        _, x, y = heap.heap_pop()
        result.append([x, y])
    return result
