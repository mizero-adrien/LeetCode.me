from typing import List
class Solution:
    def findKthPositive(self, arr: List[int], k:int)->int:
        for i in range(len(arr)):
            missing = arr[i]-(i+1)
            
            if missing>=k:
              return k+i
        
        return k+len(arr)
    
sol = Solution()
print(sol.findKthPositive([2,3,4,7,11],5))    