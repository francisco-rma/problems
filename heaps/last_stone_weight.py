from heap import Heap


def lastStoneWeight(stones: list[int]) -> int:
    heap = Heap(source=stones, order="max")

    while len(heap) > 1:
        print(heap)

        x = heap.heap_pop()
        y = heap.heap_pop()

        print(heap)

        if x == y:
            continue

        heap.heap_push(abs(x - y))
        print(heap)

    return heap[0] if heap else 0


stones = stones = [10, 4, 2, 10, 5]
result = lastStoneWeight(stones=stones)
