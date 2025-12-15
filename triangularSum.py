from typing import List
class Solution:
    def triangularSum(self, nums: List[int]) -> int:

        while len(nums)>1:
            newNums = []
            for i in range(len(nums)-1):
                newNums.append((nums[i] + nums[i+1]) % 10)

            nums = newNums
        return nums[0]

sol = Solution() 
print(sol.triangularSum([1,2,3,4,5]))   
