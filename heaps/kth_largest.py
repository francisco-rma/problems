class KthLargest:
    def _siftdown(source: list[int], start_pos: int, pos: int):
        value = source[pos]
        while pos > start_pos:
            parent_pos = (pos - 1) // 2
            if source[parent_pos] > value:
                source[pos] = source[parent_pos]
                pos = parent_pos
                continue
            break
        source[pos] = value

    def _siftup(source: list[int], idx: int):
        if not source:
            return
        upper_bound = len(source)
        start_idx = idx
        child_idx = 2 * idx + 1
        value = source[idx]

        while child_idx < upper_bound:
            sibling_idx = child_idx + 1
            if sibling_idx < upper_bound and source[sibling_idx] < source[child_idx]:
                child_idx = sibling_idx

            source[idx] = source[child_idx]

            idx = child_idx
            child_idx = 2 * idx + 1

        source[idx] = value

        KthLargest._siftdown(source=source, start_pos=start_idx, pos=idx)

    def __init__(self, k: int, nums: list[int]):
        self.source = nums
        self.k = k

        for i in range(len(self.source) // 2, -1, -1):
            KthLargest._siftup(source=self.source, idx=i)

    def pop(self) -> int:
        leaf = self.source.pop()
        if self.source:
            min_val = self.source[0]
            self.source[0] = leaf
            KthLargest._siftup(source=self.source, idx=0)
            return min_val
        return leaf

    def push(self, item: int):
        self.source.append(item)

        KthLargest._siftdown(self.source, 0, len(self.source) - 1)

    def add(self, val: int) -> int:
        self.push(val)
        while len(self.source) > self.k:
            self.pop()
        kth_largest = self.source[0]

        return kth_largest


sample_source = [1, 2, 3, 3]
k = 3
sample_stream = [3, 5, 6, 7, 8]

heap = KthLargest(k=k, nums=sample_source)

print(heap.source)
for val in sample_stream:
    heap.add(val=val)
print(heap.source)
