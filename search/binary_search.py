def binary_search(nums: list[int], target: int) -> int:
    start = 0
    end = len(nums) - 1
    i = start + ((end - start) // 2)

    while start <= end:
        test = nums[i]

        if nums[i] == target:
            return i

        elif nums[i] > target:
            end = i - 1

        else:
            start = i + 1

        i = start + ((end - start) // 2)

    return -1


nums = [-1, 0, 2, 4, 6, 8]
target = 3

result = binary_search(nums=nums, target=target)

print(result)
