import heapq
from bisect import insort_right
from random import choices, randint
from time import perf_counter

import matplotlib.pyplot as plt
from heap import MaxHeap, MinHeap


class BisectMedianFinder:
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
        if self.large_heap and num > self.large_heap[0]:
            self.large_heap.heap_push(num)
        else:
            self.small_heap.heap_push(num)

        if len(self.small_heap) - len(self.large_heap) > 1:
            small_max = self.small_heap.heap_pop()
            self.large_heap.heap_push(small_max)

        if len(self.large_heap) - len(self.small_heap) > 1:
            large_min = self.large_heap.heap_pop()
            self.large_heap.heap_push(large_min)

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


class NativeHeapMedianFinder:
    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0


def basic_test():
    bisectMedianFinder = BisectMedianFinder()
    heapMedianFinder = HeapMedianFinder()

    i = 0
    while i < 10_000:
        print(f"#{i}...")
        value = randint(0, 1_000_000)

        start = perf_counter()
        bisectMedianFinder.addNum(value)
        end = perf_counter()
        print(f"Bisect insertion time: {(end - start):.4f} seconds")

        start = perf_counter()
        heapMedianFinder.addNum(value)
        end = perf_counter()
        print(f"Heap insertion time: {(end - start):.4f} seconds")

        assert bisectMedianFinder.findMedian() == heapMedianFinder.findMedian()
        i += 1


def benchmark():
    bisectMedianFinder = BisectMedianFinder()
    heapMedianFinder = BisectMedianFinder()
    nativeHeapMedianFinder = NativeHeapMedianFinder()

    sizes = range(0, 100_000, 10_000)
    population = range(1_000_000)

    bisectTimes = []
    nativeHeapTimes = []
    heapTimes = []

    i = 0
    while i < len(sizes):
        n = sizes[i]
        print(f"\n-----Size {n}-----\n")

        source = choices(population=population, k=n)

        start = perf_counter()
        for value in source:
            bisectMedianFinder.addNum(value)
        end = perf_counter()
        timespan = end - start
        bisectTimes.append(timespan)
        print(f"bisectMedianFinder | {timespan} seconds")

        start = perf_counter()
        for value in source:
            nativeHeapMedianFinder.addNum(value)
        end = perf_counter()
        timespan = end - start
        nativeHeapTimes.append(timespan)
        print(f"nativeHeapMedianFinder | {timespan} seconds")

        start = perf_counter()
        for value in source:
            heapMedianFinder.addNum(value)
        end = perf_counter()
        timespan = end - start
        heapTimes.append(timespan)
        print(f"heapMedianFinder | {timespan} seconds")

        i += 1

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, bisectTimes, label="Bisect Median Finder")
    plt.scatter(sizes, nativeHeapTimes, label="Native Heap Median Finder")
    plt.scatter(sizes, heapTimes, label="Python Heap Median Finder")
    plt.xlabel("Number of Elements (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Performance Comparison of Median Finders")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    benchmark()
    print("PASSED")
