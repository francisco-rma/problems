from typing import Sequence


def bubble_sort(numbers: Sequence[int]) -> Sequence[int]:
    for i, value1 in enumerate(numbers):
        for j, value2 in enumerate(numbers[: len(numbers) - (i + 1)]):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers


print(
    bubble_sort(
        [
            1,
            5,
            8,
            4,
            2,
            45,
            2,
        ]
    )
)
print(
    bubble_sort(
        [
            1,
            5,
            8,
            4,
            2,
            45,
            2,
        ]
    )
)
