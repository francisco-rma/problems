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


def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    A, B = nums1, nums2

    if len(A) > len(B):
        A, B = B, A

    half = (len(A) + len(B)) // 2

    left, right = 0, len(A) - 1

    while True:
        i = left + ((right - left) // 2)
        j = half - i - 2

        leftA = A[i] if i >= 0 else float("-infinity")
        leftB = B[j] if j >= 0 else float("-infinity")
        rightA = A[i + 1] if (i + 1) < len(A) else float("infinity")
        rightB = B[j + 1] if (j + 1) < len(B) else float("infinity")

        if leftA > rightB:
            right = i - 1

        elif leftB > rightA:
            left = i + 1

        else:
            if (len(A) + len(B)) % 2 == 0:
                return (max(leftA, leftB) + min(rightA, rightB)) / 2
            else:
                return min(rightA, rightB)


nums1 = [1, 2]
nums2 = [3]

result = findMedianSortedArrays(nums1=nums1, nums2=nums2)

print(result)
