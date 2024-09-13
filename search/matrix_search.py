from operator import concat


def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    import binary_search

    nums = []
    for i in range(len(matrix)):
        nums += matrix[i]

    return binary_search.binary_search(nums=nums, target=target) != -1


matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]

target = 10

result = searchMatrix(matrix=matrix, target=target)
print(result)
