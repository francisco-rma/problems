import math


def evalRPN(tokens: list[str]) -> int:
    operators = set(["+", "-", "*", "/"])
    eval_stack = []

    for token in tokens:
        if token not in operators:

            continue

        operand2 = eval_stack.pop()
        operand1 = eval_stack.pop()
        result = None
        match token:
            case "+":
                result = operand1 + operand2
                print(f"Operation: {operand1} + {operand2} = {result}")
                pass
            case "-":
                result = operand1 - operand2
                print(f"Operation: {operand1} - {operand2} = {result}")
                pass
            case "*":
                result = operand1 * operand2
                print(f"Operation: {operand1} * {operand2} = {result}")
                pass
            case "/":
                result = operand1 / operand2
                result = math.floor(result) if result >= 0 else math.ceil(result)
                print(f"Operation: {operand1} / {operand2} = {result}")
                pass

        eval_stack.append(result)
        print(eval_stack)

    return eval_stack[0]


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]


result = evalRPN(tokens)

print(result)
