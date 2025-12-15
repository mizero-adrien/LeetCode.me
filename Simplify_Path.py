class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = [] 
        parts = path.split('/') 
        
        for part in parts:
            if part == '' or part == '.':  # skip empty or current directory
                continue
            elif part == '..':  # go up one level if possible
                if stack:
                    stack.pop()
            else:  # valid directory or file name
                stack.append(part)
        
        # join the stack to form canonical path
        return '/' + '/'.join(stack)
sol = Solution()

        