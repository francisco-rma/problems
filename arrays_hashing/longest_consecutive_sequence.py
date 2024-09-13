from typing import List


def longestConsecutive(nums: List[int]) -> int:
    members = {}
    max_sequence = 0
    i = 0
    while i < len(nums):
        if nums[i] in members:
            i += 1
            continue

        members[nums[i]] = nums[i]
        i += 1

    for index, element in enumerate(nums):
        if element - 1 in members:
            continue

        sequence = [element]
        number = nums[index] + 1
        while number in members:
            sequence.append(number)
            number += 1

        max_sequence = max(max_sequence, len(sequence))

    return max_sequence


nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
nums = [9, 1, -3, 2, 4, 8, 3, -1, 6, -2, -4, 7]
nums = [100, 4, 200, 1, 3, 2]

print(longestConsecutive(nums=nums))
