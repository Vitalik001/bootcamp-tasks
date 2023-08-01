class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque

        stack = deque()

        for el in s:
            if el in ("(", "{", "["):
                stack.append(el)
            elif stack:
                right = stack.pop()
                if right+el not in ("()", "{}", "[]"):
                    return False
            else:
                return False
        return False if stack else True
