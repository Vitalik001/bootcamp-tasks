import collections


class MyStack:

    def __init__(self):
        self.stack = collections.deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        for _ in range(len(self.stack) - 1):
            self.stack.append(self.stack.popleft())
        return self.stack.popleft()

    def top(self) -> int:
        for _ in range(len(self.stack) - 1):
            self.stack.append(self.stack.popleft())
        element = self.stack.popleft()
        self.stack.append(element)
        return element

    def empty(self) -> bool:
        return len(self.stack) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()