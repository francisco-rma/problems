from typing import List


def product_except_self(nums: List[int]):
    def find_prefix(numbers: List[int]) -> List[int]:
        prefix = [1]
        i = 0

        while i < len(numbers):
            prefix.append(numbers[i] * prefix[i])
            i += 1

        return prefix

    def find_postfix(numbers: List[int]) -> List[int]:
        postfix = [1] * (len(numbers) - 1)
        postfix.append(1)
        i = len(numbers) - 1

        while i > 0:
            postfix[i - 1] = numbers[i] * postfix[i]
            i -= 1

        postfix[-1] = 1

        return postfix

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
