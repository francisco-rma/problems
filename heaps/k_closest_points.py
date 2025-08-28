import math
from heaps.heap import Heap


def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    heap = Heap([[math.sqrt(x**2 + y**2), x, y] for x, y in points])
    print(heap)
    result = []
    for _ in range(k):
        _, x, y = heap.heap_pop()
        result.append([x, y])
    print(result)
    return result


if __name__ == "__main__":
    k_closest([[1, 3], [-2, 2], [2, -2], [3, 3], [-1, -4], [0, 0], [0, 1], [1, 0], [1, 1]], 1)
    k_closest([[3, 3], [5, -1], [-2, 4], [-1, 1], [2, -2], [0, 0], [0, 1], [1, 0], [1, 1]], 1)
