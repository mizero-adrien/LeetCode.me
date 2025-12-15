from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        #one children must receive cookie<=1
        s.sort()
        g.sort()

        i=0
        j=0
        count =0
        while i<len(g) and j<len(s):
            if s[j]>=g[i]:  #check if cookie can satisfy child

                i+=1   #child satisfied
                j+=1    
                count+=1
            else:
                j+=1  # move cookie pointer
        return count   