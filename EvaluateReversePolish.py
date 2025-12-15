from typing import List
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:  # token == "/"
                    # use int() to truncate toward zero
                    stack.append(int(a / b))
            else:
                stack.append(int(token))

        return stack[0]
tokens = ["2","1","+","3","*"]
print(Solution().evalRPN(tokens))