from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = n*(n+1)//2
        return expected - sum(nums)

sol = Solution()
print(sol.missingNumber([3,0,1]))

#another way
class Solution:
    def missingNumber(self, nums):
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
