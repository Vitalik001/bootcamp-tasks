import collections


class MinStack:

    def __init__(self):
        self.stack = collections.deque()

    def push(self, val: int) -> None:
        self.stack.append((val, min(self.getMin() if len(self.stack)>0 else float("inf"), val)))

    def pop(self) -> None:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()