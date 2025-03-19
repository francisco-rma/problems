def findMin(nums: list[int]) -> int:
    def find_pivot_index(values: list[int]) -> int | None:
        left, right = 0, len(nums) - 1
        while left <= right:
            idx = left + ((right - left) // 2)

            if nums[idx] < nums[idx - 1]:
                return idx
                break

            elif nums[idx] < nums[0]:
                right = idx - 1

            else:
                left = idx + 1

        return None

    pivot_index = find_pivot_index(nums)

    if pivot_index is not None:
        return nums[pivot_index]

    return nums[0]


nums = [4, 5, 6, 7]

result = findMin(nums=nums)

print(result)
