def contains_duplicate(nums: list[int]) -> bool:
    counter = {}
    for index, value in enumerate(nums):
        if value not in counter:
            counter[value] = 1
            continue

        counter[value] += 1

        if counter[value] > 1:
            return True

    return False
