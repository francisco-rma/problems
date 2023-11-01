from typing import List


def product_except_self(nums: List[int]):
    def product(numbers: List[int]) -> int | None:
        if len(numbers) == 0:
            return None

        if len(numbers) == 1:
            return numbers[0]

        value = numbers[0]
        for num in numbers[1:]:
            value *= num
        return value

    def find_prefix(numbers: List[int]) -> List[int]:
        prefix = [numbers[0]]
        i = 1

        while i < len(numbers):
            prefix.append(numbers[i - 1] * prefix[i - 1])
            i += 1

        prefix[0] = 1

        return prefix

    def find_postfix(numbers: List[int]) -> List[int]:
        postfix = [0] * (len(numbers) - 1)
        postfix.append(1)
        i = len(numbers) - 2

        while i >= 0:
            postfix[i] = numbers[i + 1] * postfix[i + 1]
            i -= 1

        postfix[-1] = 1

        return postfix

    def zero_indices(numbers: List[int]) -> tuple:
        zero_indices = []
        for index, value in enumerate(numbers):
            if value == 0:
                zero_indices[0].append(index)
        return zero_indices

    # prefix = find_prefix(nums)
    # postfix = find_postfix(nums)

    products = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        products[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        products[i] *= postfix
        postfix *= nums[i]

    return products


nums = [-1, 1, 0, -3, 3]

products = product_except_self(nums=nums)

print(products)
