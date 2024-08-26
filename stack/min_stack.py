class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []
        pass

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min or self.min[-1] >= val:
            self.min.append(val)
        pass

    def pop(self) -> None:
        a = self.stack.pop()
        if a == self.min[-1]:
            self.min.pop()
        pass

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.stack and self.min:
            return self.min[-1]


stack = MinStack()
stack.push(1)
stack.push(2)
stack.push(0)
min_value = stack.getMin()
print(min_value)
stack.pop()
stack.top()
min_value = stack.getMin()
print(min_value)
