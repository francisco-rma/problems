def smallest_missing(source: list[int]):
    sorted_source = sorted(set(filter(lambda x: x > 0, source)))
    result = 0
    for idx, item in enumerate(sorted_source):
        diff = abs(item - result)
        if diff > 1:
            break
        result = item

    result += 1
    return result


if __name__ == "__main__":
    source = [1, 2, 3, 4, 5, 6, 7, 8]
    control = 9

    test = smallest_missing(source)

    assert test == control

    print("source: ", source)
    print("test: ", test)
    print("control: ", control)
