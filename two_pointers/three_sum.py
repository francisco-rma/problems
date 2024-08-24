from datetime import datetime
from matplotlib import pyplot as plt


def slow_three_sum(nums: list[int]) -> set[tuple[int]]:
    result_set = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    result_set.add(tuple(sorted([nums[i], nums[j], nums[k]])))
    return result_set


def threeSum(nums: list[int]) -> set[tuple[int]]:
    def two_sum(nums: list[int], target: int) -> set[tuple[int]]:
        indices = set()
        complements = {}

        for index, value in enumerate(nums):
            complement = target - value
            if complement in complements:
                indices.add(tuple(sorted([complements[complement], index])))
            complements[value] = index
        return indices

    result_set = set()
    for i in range(len(nums)):
        subset = (nums[:i] if i > 0 else []) + nums[i + 1 :]
        result = two_sum(subset, -nums[i])

        if not result:
            continue

        for start, end in result:
            result_set.add(
                tuple(
                    sorted(
                        [
                            nums[i],
                            nums[(start if start < i else start + 1)],
                            nums[(end if end < i else end + 1)],
                        ]
                    )
                )
            )

    return result_set


def three_sum_v2(nums: list[int], sort=False) -> set[tuple[int]]:
    def twoSum(numbers: list[int], target: int) -> set[tuple[int]]:
        left = 0
        right = len(numbers) - 1
        result_set = set()
        while left < right:
            current_sum = numbers[right] + numbers[left]
            if current_sum == target:
                result_set.add(tuple([left, right]))
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                left += 1

        return result_set if len(result_set) > 0 else None

    if sort:
        nums.sort()
    result_set = set()
    for i in range(len(nums)):
        subset = (nums[:i] if i > 0 else []) + nums[i + 1 :]
        result = twoSum(subset, -nums[i])

        if not result:
            continue

        for item in result:
            start, end = item[0], item[1]
            result_set.add(
                tuple(
                    sorted(
                        [
                            nums[i],
                            nums[(start if start < i else start + 1)],
                            nums[(end if end < i else end + 1)],
                        ]
                    )
                )
            )

    return result_set


# Test for performance
size_coefficient = []
fast_results = []
slow_results = []
even_faster_results = []
even_faster_but_sorting_results = []

base_set = [-1, 0, 1, 2, -1, -4]

for i in range(1, 50):
    array = base_set * i
    sorted_array = sorted(array)

    fast_start = datetime.now()
    fast_result = threeSum(array)
    fast_end = datetime.now()

    even_faster_start = datetime.now()
    even_faster_result = three_sum_v2(sorted_array)
    even_faster_end = datetime.now()

    even_faster_but_sorting_start = datetime.now()
    even_faster_but_sorting_result = three_sum_v2(array, sort=True)
    even_faster_but_sorting_end = datetime.now()

    slow_start = datetime.now()
    slow_result = slow_three_sum(array)
    slow_end = datetime.now()

    assert (
        fast_result.symmetric_difference(slow_result) == set()
        and fast_result.symmetric_difference(even_faster_result) == set()
    )

    size_coefficient.append(i * len(base_set))
    fast_results.append((fast_end - fast_start).total_seconds())
    even_faster_results.append((even_faster_end - even_faster_start).total_seconds())
    even_faster_but_sorting_results.append(
        (even_faster_but_sorting_end - even_faster_but_sorting_start).total_seconds()
    )
    slow_results.append((slow_end - slow_start).total_seconds())

    print(f"Iteration #{i}")
    print(f"slow: {slow_end - slow_start}")
    print(slow_result)
    print(f"fast: {fast_end - fast_start}")
    print(fast_result)
    print(f"even faster: {even_faster_end - even_faster_start}")
    print(even_faster_result)
    print(
        f"even faster but sorting: {even_faster_but_sorting_end - even_faster_but_sorting_start}"
    )
    print(even_faster_but_sorting_result)
    print("\n" + "-" * 50 + "\n")


plt.plot(size_coefficient, slow_results, label="Slow")
plt.plot(size_coefficient, fast_results, label="Fast")
plt.plot(size_coefficient, even_faster_results, label="Even faster")
plt.plot(
    size_coefficient, even_faster_but_sorting_results, label="Even faster but sorting"
)
plt.legend()
plt.show()
