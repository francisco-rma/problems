def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
    def binary_count(values: list[int], target: int) -> int:
        if not values or values[-1] < target:
            None

        left = 0

        right = len(values) - 1

        while left <= right:
            midpoint = left + ((right - left) // 2)

            if values[midpoint] <= target and values[midpoint + 1] > target:
                return midpoint

            elif values[midpoint] < target:
                left = midpoint + 1

            else:
                right = midpoint - 1

        return 0

    first = None
    second = None

    if nums1[0] < nums2[0]:
        first = nums1
        second = nums2

    elif nums1[0] == nums2[0]:
        if nums1[-1] <= nums2[-1]:
            first = nums1
            second = nums2
    else:
        first = nums2
        second = nums1

    m, n = len(first), len(second)

    left, right = 0, n + m - 1

    midpoint = left + ((right - left) // 2)

    while left <= right:
        idx1 = binary_count(values=first, target=midpoint)
        idx2 = binary_count(values=second, target=midpoint)

        left_count1, right_count1 = idx1 + 1, len(first) - (idx1 + 1)
        left_count2, right_count2 = idx2 + 1, len(second) - (idx2 + 1)

        diff = abs((left_count1 + left_count2) - (right_count1 + right_count2)) <= 1

        if diff == 0:
            res = 0
            if midpoint < m:
                res = first[midpoint]
            return

        elif diff == 1:
            res1 = 0
            res2 = 0
            if midpoint < m:
                res1 = first[[midpoint]]
                pass

        elif diff > 1:
            pass

        else:
            pass

    pass
