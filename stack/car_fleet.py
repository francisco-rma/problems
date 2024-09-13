def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    """
    target = 10
    position: [1,4]
    speed: [3,2]

    t = 0:
    [
    0,
    1, -> 1
    2,
    3,
    4, -> 2
    5,
    6,
    7,
    8,
    9,
    10
    ]

     ----

    t = 1:
    [
    0,
    1,
    2,
    3,
    4, -> 1
    5,
    6, -> 2
    7,
    8,
    9,
    10
    ]

    ----

    t = 2:
    [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7, -> 1
    8, -> 2
    9,
    10
    ]

    ----

    t = 3:
    [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10 -> 1,2
    ]
    """

    stack = []

    for pos, spd in sorted(list(map(list, zip(position, speed))), key=(lambda x: x[0]))[
        ::-1
    ]:
        stack.append((target - pos) / spd)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)


target = 10
position = [8, 3, 7, 4, 6, 5]
speed = [4, 4, 4, 4, 4, 4]


fleets = carFleet(target=target, position=position, speed=speed)

print(fleets)
