import math
from heaps.heap import Heap


def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    heap = Heap(list(map(lambda x: math.sqrt(x[0] ** 2 + x[1] ** 2), points)))
    print(heap)
    result = [heap.heap_pop() for _ in range(k)]
    print(result)
    return result


if __name__ == "__main__":
    kClosest([[1, 3], [-2, 2], [2, -2], [3, 3], [-1, -4], [0, 0], [0, 1], [1, 0], [1, 1]], 1)
    kClosest([[3, 3], [5, -1], [-2, 4], [-1, 1], [2, -2], [0, 0], [0, 1], [1, 0], [1, 1]], 1)
