def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
    max_num = max(candies)
    return ((value + extraCandies) >= max_num for value in candies)
