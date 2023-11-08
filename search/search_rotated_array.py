from typing import List
import binary_search


def find_pivot_index(nums: List[int]) -> int:
    start = 0
    end = len(nums) - 1
    while start < end:
        midpoint = (end + start) // 2
        if nums[midpoint + 1] < nums[midpoint]:
            return midpoint
        elif nums[midpoint + 1] < nums[0]:
            end = midpoint
        else:
            start = midpoint + 1

    index = -1
    return index


def search_rotated_array(nums: List[int], target: int) -> int:
    index = -1

    pivot_index = find_pivot_index(nums=nums)

    if pivot_index == -1:
        index = binary_search.binary_search(nums, target)
        return index

    a = nums[pivot_index + 1]
    b = nums[-1]

    if nums[pivot_index] == target:
        return pivot_index

    elif nums[0] <= target <= nums[pivot_index]:
        index = binary_search.binary_search(nums=nums[: pivot_index + 1], target=target)

    elif a <= target <= b:
        index = binary_search.binary_search(nums=nums[pivot_index + 1 :], target=target)
        if index != -1:
            index += pivot_index + 1

    else:
        index = -1

    return index


test = [4, 5, 6, 7, 0, 1, 2]
test = [5, 1, 3]


# pivot_index = find_pivot_index(test)
# print(pivot_index)

index = search_rotated_array(test, target=2)

print(index)
