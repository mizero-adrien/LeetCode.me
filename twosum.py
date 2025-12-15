from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)

        for i in range(n):
            for j in range(i+1,n):
                if nums[i] + nums[j]==target:
                    return [i,j]
        

num = [2,7,11,15]
target = 9

def TwoSum(self, nums:List[int], target: int)->List[int]:
    left =0
    right = len(nums)-1
    while left<right:
        s = nums[left] + nums[right]
        if s == target:
            return [left,right]
        elif s<target:
            left+=1
        else:
            right-=1
    return [-1,-1]        
            
            