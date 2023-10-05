class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        size = len(flowerbed)
        for idx, value in enumerate(flowerbed):
            placeable = False
            if idx == 0:
                placeable = (value == 0 and flowerbed[idx+1] == 0)
            elif idx < size - 1:
                placeable = (
                    value == 0 and flowerbed[idx+1] == 0 and flowerbed[idx-1] == 0)
            else:
                placeable = (value == 0 and flowerbed[idx-1] == 0)
            if placeable:
                flowerbed[idx] = 1
                n -= 1

        return n == 0


solution = Solution()

test = solution.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2)

print(test)
