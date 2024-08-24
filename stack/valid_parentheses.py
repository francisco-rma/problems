def isValid(s: str) -> bool:
    def is_match(opening, closing) -> bool:
        match opening:
            case "(":
                return closing == ")"
            case "[":
                return closing == "]"
            case "{":
                return closing == "}"
            case _:
                return False

    stack = []
    stack.append(s[0])

    for char in s[1:]:
        if len(stack) > 0 and is_match(stack[-1], char):
            stack.pop()
        else:
            stack.append(char)

    return len(stack) == 0


test = "[]"
check = isValid(test)
print(check)
