class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Step 1: find the first occurrence of ch
        index = word.find(ch)
        
        # Step 2: if ch not found, return original word
        if index == -1:
            return word
        
        # Step 3: reverse the prefix and append the rest
        return word[:index+1][::-1] + word[index+1:]
 
 #stack approach
#  class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        n = len(word)
        found = False  # Flag to mark when we find ch
        
        # Step 1: Traverse the word
        for i in range(n):
            stack.append(word[i])
            if word[i] == ch:
                found = True
                break  # Stop adding once we find ch
        
        # Step 2: If ch not found, return original word
        if not found:
            return word
        
        # Step 3: Pop stack to get reversed prefix
        reversed_prefix = ""
        while stack:
            reversed_prefix += stack.pop()
        
        # Step 4: Append remaining part of the word
        remaining = word[i+1:]  # i is index of ch
        return reversed_prefix + remaining
