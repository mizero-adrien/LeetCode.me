from typing import List
class Solution:
    def removeElement(self, nums: List[int], val : int)->int:
        k=0 # count element that is not equal to val
        for num in nums:
            if num == val:
                nums[k] = num
                k+=1
        return k
            
        