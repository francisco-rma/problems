def isValid(s: str) -> bool:
    key_map = {")": "(", "}": "{", "]": "["}

    stack = []

    for char in s:
        if char not in key_map:
            stack.append(char)
            continue
        if len(stack) == 0 or stack[-1] != key_map[char]:
            return False

        stack.pop()

    return len(stack) == 0


test = "[]"
check = isValid(test)
print(check)
