class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == '+':
                x = stack.pop()
                y = stack.pop()
                stack.append(x+y)
            elif c == '*':
                x = stack.pop()
                y = stack.pop()
                stack.append(x*y)
            elif c == '-':
                x = stack.pop()
                y = stack.pop()
                stack.append(y-x)
            elif c == '/':
                x = stack.pop()
                y = stack.pop()
                stack.append(int(y/x))
            else:
                stack.append(int(c))
        return stack.pop()

            