from operator import concat
from typing import List


def binary_search(nums: List[int], target: int) -> int:
    start = 0
    end = len(nums) - 1

    while start <= end:
        midpoint = (end + start) // 2
        if nums[midpoint] == target:
            return midpoint
        elif nums[midpoint] > target:
            end = midpoint - 1
        else:
            start = midpoint + 1

    index = -1
    return index
