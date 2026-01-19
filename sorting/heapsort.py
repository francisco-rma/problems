from heaps.heap import MaxHeap, max_heapify


def heapsort(source: list[int]):
    n = len(source)
    heap = MaxHeap(source=source, limit=n)
    assert heap.limit is not None
    for i in range(n - 1, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        heap.limit -= 1
        max_heapify(heap, 0)


if __name__ == "__main__":
    source = [1, 3, 2, 4, 7, 9, 8, 16, 14, 10]
    print(source)
    heapsort(source)
    print(source)
    assert source == sorted(source)
