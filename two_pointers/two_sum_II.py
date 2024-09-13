from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers) - 1

    while left <= right:
        current_sum = numbers[right] + numbers[left]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum > target:
            right -= 1
        else:
            left += 1


array = [2, 7, 11, 15]
target = 13

print(twoSum(array, target))
