from heap import Heap


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.source: Heap = Heap(source=nums, order="min")
        self.k = k

    def add(self, val: int) -> int:
        self.source.heap_push(val)
        while len(self.source) > self.k:
            self.source.heap_pop()
        kth_largest = self.source[0]

        return kth_largest
