from bisect import insort_right
from random import randint

from heap import MaxHeap, MinHeap


class MedianFinder:
    def __init__(self):
        self.values = []

    def addNum(self, num: int) -> None:
        insort_right(self.values, num)

    def findMedian(self) -> float:
        n = len(self.values)
        if n == 0:
            raise ValueError("Value list is empty")
        if n == 1:
            return self.values[0]

        i = n // 2

        if n % 2 == 0:
            return (self.values[i] + self.values[i - 1]) / 2.0

        else:
            return self.values[i]


class HeapMedianFinder:
    def __init__(self):
        self.small_heap = MaxHeap(source=[])
        self.large_heap = MinHeap(source=[])

    def addNum(self, num: int) -> None:
        self.small_heap.heap_push(num)
        small_n = len(self.small_heap)
        large_n = len(self.large_heap)

        if small_n - large_n > 1:
            small_max = self.small_heap.heap_pop()
            self.large_heap.heap_push(small_max)

        small_n = len(self.small_heap)
        large_n = len(self.large_heap)

        if large_n - small_n > 1:
            large_min = self.large_heap.heap_pop()
            self.large_heap.heap_push(large_min)

        if small_n > 0 and large_n > 0 and self.small_heap[0] > self.large_heap[0]:
            large_min = self.large_heap.heap_pop()
            small_max = self.small_heap.heap_pop()

            self.small_heap.heap_push(large_min)
            self.large_heap.heap_push(small_max)

    def findMedian(self) -> float:
        small_n = len(self.small_heap)
        large_n = len(self.large_heap)

        if small_n < 1:
            raise ValueError("No values")

        if small_n > large_n:
            return self.small_heap[0]
        elif large_n > small_n:
            return self.large_heap[0]
        else:
            return (self.large_heap[0] + self.small_heap[0]) / 2.0


def basic_test():
    bisectMedianFinder = MedianFinder()
    heapMedianFinder = HeapMedianFinder()

    i = 0
    while i < 1000:
        value = randint(0, 1_000_000)
        bisectMedianFinder.addNum(value)
        heapMedianFinder.addNum(value)

        assert bisectMedianFinder.findMedian() == heapMedianFinder.findMedian()
        i += 1


if __name__ == "__main__":
    basic_test()
    print("PASSED")
