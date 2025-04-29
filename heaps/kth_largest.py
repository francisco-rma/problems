from heap import Heap


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = Heap(nums)

    def add(self, val: int) -> int: ...
