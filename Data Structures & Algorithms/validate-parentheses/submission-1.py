class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeOpen = {")" : "(", "]":"[", "}":"{"}
        for first in s:
            if first in closeOpen:
                if stack and stack[-1] == closeOpen[first]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(first)
        return True if not stack else False