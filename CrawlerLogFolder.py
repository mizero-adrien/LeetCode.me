from typing import List
#using stack 
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        
        for log in logs:
            if log == "../":
                if stack:
                    stack.pop()     # Go to parent directory
            elif log == "./":
                continue            # Stay in same directory
            else:
                stack.append(log)   # Enter a child directory
        
        return len(stack)
    
 #using normal array method
#  class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        
        for log in logs:
            if log == "../":
                if depth > 0:   # Can't go above main folder
                    depth -= 1
            elif log == "./":
                continue       # Stay in same folder
            else:
                depth += 1     # Enter a child folder
        
        return depth
