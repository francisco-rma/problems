def parity_sort(values: list[int]) -> list[int]:
    next_even, next_odd = 0, len(values) - 1
    while next_even < next_odd:
        if values[next_even] % 2 == 0:
            next_even += 1
        else:
            values[next_even], values[next_odd] = values[next_odd], values[next_even]
            next_odd -= 1

    return values


def validation(values: list[int]) -> bool:
    if not values:
        return True

    status = values[0] % 2
    can_change = status == 0
    idx = 1

    while idx < len(values):
        cur_status = values[idx] % 2
        if cur_status != status:
            if not can_change:
                return False
            else:
                can_change = False

            status = cur_status
        idx += 1

    return True
