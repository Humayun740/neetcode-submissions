class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '(':
                stack.append(c)

            elif c == '[':
                stack.append(c)

            elif c == '{':
                stack.append(c)

            elif c == '}':
                if not stack:
                    return False

                x = stack.pop()
                if x != '{':
                    return False

            elif c == ']':
                if not stack:
                    return False

                x = stack.pop()
                if x != '[':
                    return False

            elif c == ')':
                if not stack:
                    return False

                x = stack.pop()
                if x != '(':
                    return False

        return len(stack) == 0