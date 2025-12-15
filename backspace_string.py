class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(text):
            stack =[]
            for char in text:
                if char != "#":
                    stack.append(char)
                elif stack:
                    stack.pop()
            return "".join(stack)
        return build(s) == build(t)
sol = Solution()
print(sol.backspaceCompare("ab#c", "ad#c"))  

#second alternative with space and time complexity of o(n) and o(1) respectively

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        skipS = skipT = 0

        while i >= 0 or j >= 0:
            # Move i in s
            while i >= 0:
                if s[i] == '#':
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break

            # Move j in t
            while j >= 0:
                if t[j] == '#':
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break

            # Compare current characters
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False

            # If only one pointer is valid
            if (i >= 0) != (j >= 0):
                return False

            i -= 1
            j -= 1
        
        return True
