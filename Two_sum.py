from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}  
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i

#using two pointer
def two_sum_two_pointers(nums, target):
    # Initialize pointers
    left = 0
    right = len(nums) - 1
    
    # Loop until the pointers meet
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            return [left, right]
        
        elif current_sum > target:
            # Sum is too big, decrease right pointer to get smaller numbers
            right -= 1
            
        else: # current_sum < target
            # Sum is too small, increase left pointer to get bigger numbers
            left += 1
            
    return []

# Test
print(two_sum_two_pointers([2, 7, 11, 15], 9))
# Output: [0, 1]