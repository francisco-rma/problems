# =======================================================
# Test harness
# =======================================================


# =======================================================
# Heapify
# =======================================================

import random
from heap import Heap


def test_max_heap(sample: list[int]):
    max_val = max(sample)
    heap = Heap.build_heap(sample, order="max")

    for i in range(len(heap) // 2):
        assert heap[0] == max_val
        assert heap[i] >= heap[2 * i + 1]
        if (2 * i + 2) < len(heap):
            assert heap[i] >= heap[2 * i + 2]


def test_min_heap(sample: list[int]):
    min_val = min(sample)
    heap = Heap.build_heap(sample, order="min")

    for i in range(len(heap) // 2):
        assert heap[0] == min_val
        assert heap[i] <= heap[2 * i + 1]
        if (2 * i + 2) < len(heap):
            assert heap[i] <= heap[2 * i + 2]


def multi_test():
    population = range(1000)
    i = 0
    while i < 100:
        sample = random.sample(population=population, k=random.randint(50, 500))
        heap = Heap(source=sample)
        print(f"MIN: {min(sample)} - MAX: {max(sample)}\n")
        test_max_heap(sample=heap)
        print(f"Max heap start: {heap[0]}")
        print(f"Max heap end: {heap[-1]}")
        test_min_heap(sample=heap)
        print(f"Min heap start: {heap[0]}")
        print(f"Min heap end: {heap[-1]}")
        print("\n---------\n")
        i += 1
        print(heap)


def heap_pop_test():
    # sample = random.sample(population=range(1000), k=10)
    sample = [211, 278, 741, 381, 525, 767, 827, 476, 782, 802]
    control = sorted([211, 278, 741, 381, 525, 767, 827, 476, 782, 802], reverse=True)

    heap = Heap(source=sample)

    while heap and control:
        result = heap.heap_pop()
        assert result == control.pop(0)
        assert len(heap) == len(control)
        print(heap)
        print(f"{result} has been popped!\n")
        print(heap)
        print("\n---------\n")


def multi_heap_pop_test():
    population = range(1000)
    i = 0
    while i < 100:
        sample = random.sample(population=population, k=random.randint(50, 500))
        heap = Heap(source=sample)

        print("\n---------\n")
        i += 1
        print(heap)

    heap_pop_test()


heap_pop_test()
