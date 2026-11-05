class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for num in tokens:
            if num == '+':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a + b)
            elif num == "-":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b - a)
            elif num == "*":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a * b)
            elif num == "/":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b/a)
            else:
                stack.append(num)
        return int(stack[0])