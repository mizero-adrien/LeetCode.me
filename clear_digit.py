class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for str in s:
            if str.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(str)


        return "".join(stack)  