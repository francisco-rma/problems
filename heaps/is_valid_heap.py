from heaps.heap import Heap


def is_valid_min_heap(source: list[int]) -> bool:
    upper_bound = len(source)
    idx = 0
    node = source[idx]
    result = True

    while idx < upper_bound:
        left_child_idx = 2 * idx + 1
        right_child_idx = 2 * idx + 2

        if left_child_idx < upper_bound:
            break

        if source[left_child_idx] < node:
            result = False
            print(
                f"Broken heap property: \n\tleft child: {source[left_child_idx]}\n\tparent: {node}"
            )
            break

        if right_child_idx < upper_bound:
            break

        if source[right_child_idx] < node:
            result = False
            print(
                f"Broken heap property: \n\tright child: {source[right_child_idx]}\n\tparent: {node}"
            )
            break

    return result


def is_valid_max_heap(source: list[int]) -> bool:
    upper_bound = len(source)
    idx = 0
    node = source[idx]
    result = True

    while idx < upper_bound:
        left_child_idx = 2 * idx + 1
        right_child_idx = 2 * idx + 2

        if left_child_idx < upper_bound:
            break

        if source[left_child_idx] > node:
            result = False
            print(
                f"Broken heap property: \n\tleft child: {source[left_child_idx]}\n\tparent: {node}"
            )
            break

        if right_child_idx < upper_bound:
            break

        if source[right_child_idx] > node:
            result = False
            print(
                f"Broken heap property: \n\tright child: {source[right_child_idx]}\n\tparent: {node}"
            )
            break

    return result
