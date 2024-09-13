from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    indices = []
    complements = {}

    for index, value in enumerate(nums):
        complement = target - value
        if complement in complements:
            indices.append(complements[complement])
            indices.append(index)
            return indices
        complements[value] = index
    return indices
