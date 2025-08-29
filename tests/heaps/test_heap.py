import random
import time
import numpy as np
from heaps.heap import Heap
from heaps.k_closest_points import k_closest
from heaps.is_valid_heap import is_valid_max_heap, is_valid_min_heap

POP_SIZE = 10**5
SAMPLE_COUNT = POP_SIZE // 10


def test_valid_heap():
    source: list[int | None] = [17, 9, 50, 23, 76, 5, 12, 30, 60]
    heap: Heap = Heap(source, order="min")
    assert heap is not None
    assert heap.is_valid()


def test_max_heap():
    sample = random.sample(population=range(POP_SIZE), k=SAMPLE_COUNT)
    max_val = max(sample)
    heap = Heap(sample, order="max")

    assert heap[0] == max_val

    for i in range(len(heap) // 2):
        assert heap[i] >= heap[(2 * i) + 1]
        if (2 * i + 2) < len(heap):
            assert heap[i] >= heap[2 * i + 2]


def test_min_heap():
    sample = random.sample(population=range(POP_SIZE), k=SAMPLE_COUNT)
    min_val = min(sample)
    heap = Heap(sample, order="min")
    assert heap[0] == min_val

    for i in range(len(heap) // 2):
        assert heap[i] <= heap[(2 * i) + 1]
        if (2 * i + 2) < len(heap):
            assert heap[i] <= heap[2 * i + 2]


def test_heap_pop():
    sample = random.sample(population=range(POP_SIZE), k=SAMPLE_COUNT)
    control = sorted(sample)

    heap = Heap(source=sample, order="min")

    while heap and control:
        assert heap.is_valid()
        result = heap.heap_pop()
        assert heap.is_valid()

        control_result = control.pop(0)
        assert result == control_result
        assert len(heap) == len(control)


def test_heap_push():
    control = random.sample(population=range(POP_SIZE), k=SAMPLE_COUNT)
    heap = Heap(source=[], order="min")

    i = 0
    while len(heap) < len(control):
        idx = heap.heap_push(control[i])
        assert heap[idx] == control[i]
        assert len(heap) == len(control[: i + 1])
        i += 1


def test_min_stream():
    sample = random.sample(population=range(POP_SIZE), k=SAMPLE_COUNT)
    heap = Heap(source=sample.copy(), order="min")

    stream = [random.randint(0, 100) for _ in range(len(heap))]

    for i, instruction in enumerate(stream):
        if len(heap) == 0 or instruction % 2 != 0:
            cur_size = len(heap)
            idx = heap.heap_push(stream[i])
            assert heap[idx] == stream[i]
            assert len(heap) == cur_size + 1
        else:
            cur_size = len(heap)
            result = heap.heap_pop()
            if len(heap) > 0:
                assert result <= heap[0]
            assert len(heap) == cur_size - 1


def test_max_stream():
    sample = random.sample(population=range(POP_SIZE), k=SAMPLE_COUNT)
    heap = Heap(source=sample.copy(), order="max")

    stream = [random.randint(0, 100) for _ in range(len(heap))]

    for i, instruction in enumerate(stream):
        if len(heap) == 0 or instruction % 2 != 0:
            cur_size = len(heap)
            idx = heap.heap_push(stream[i])
            assert heap[idx] == stream[i]
            assert len(heap) == cur_size + 1
        else:
            cur_size = len(heap)
            result = heap.heap_pop()
            if len(heap) > 0:
                assert result >= heap[0]
            assert len(heap) == cur_size - 1
