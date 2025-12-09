import random

from heaps.heap import Heap, MinHeap

POP_SIZE = 10**5
SAMPLE_COUNT = POP_SIZE // 10


def test_valid_heap():
    source: list[int | None] = [17, 9, 50, 23, 76, 5, 12, 30, 60]
    hp: MinHeap = MinHeap(source)
    assert hp is not None
    assert hp.is_valid()


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
    hp = MinHeap(sample)
    assert hp[0] == min_val

    for i in range(len(hp) // 2):
        assert hp[i] <= hp[(2 * i) + 1]
        if (2 * i + 2) < len(hp):
            assert hp[i] <= hp[2 * i + 2]


def test_heap_pop():
    sample = random.sample(population=range(POP_SIZE), k=SAMPLE_COUNT)
    control = sorted(sample)

    hp = MinHeap(source=sample)

    while hp and control:
        assert hp.is_valid()
        result = hp.heap_pop()
        assert hp.is_valid(), f"{hp}"

        control_result = control.pop(0)
        assert result == control_result
        assert len(hp) == len(control)


def test_heap_push():
    control = random.sample(population=range(POP_SIZE), k=SAMPLE_COUNT)
    hp: MinHeap = MinHeap(source=[])

    i = 0
    while len(hp) < len(control):
        idx = hp.heap_push(control[i])
        assert hp[idx] == control[i]
        assert len(hp) == len(control[: i + 1])
        i += 1


def test_heap_push_limited():
    limit = 5
    source = random.sample(population=range(POP_SIZE), k=SAMPLE_COUNT)
    heap: MinHeap = MinHeap(source=[], limit=limit)

    assert heap.limit is not None and heap.limit == limit

    i = 0
    while source:
        item = source.pop()
        idx = heap.heap_push(item)
        assert heap[idx] == item
        assert len(heap) <= heap.limit
        i += 1


def test_min_stream():
    sample = random.sample(population=range(POP_SIZE), k=SAMPLE_COUNT)
    heap: MinHeap = MinHeap(source=sample.copy())

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
    hp: MinHeap = MinHeap(source=sample.copy())

    stream = [random.randint(0, 100) for _ in range(len(hp))]

    for i, instruction in enumerate(stream):
        if len(hp) == 0 or instruction % 2 != 0:
            cur_size = len(hp)
            idx = hp.heap_push(stream[i])
            assert hp[idx] == stream[i]
            assert len(hp) == cur_size + 1
        else:
            cur_size = len(hp)
            result = hp.heap_pop()
            if len(hp) > 0:
                assert result >= hp[0]
            assert len(hp) == cur_size - 1
