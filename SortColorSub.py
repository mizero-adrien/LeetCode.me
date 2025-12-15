from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:  # nums[mid] == 2
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
sol = Solution()

# We need to sort an array containing only:

# • 0 (red)
# • 1 (white)
# • 2 (blue)

# Constraints:

# • No built-in sort
# • Must be in-place
# • Preferably one pass
# • Constant extra space

# This is a classic partitioning problem.

# Dutch National Flag Algorithm
# Use three pointers:

# • low points to where the next 0 should be placed
# • mid scans the array
# • high points to where the next 2 should be placed

# Rules:

# • If nums[mid] == 0, swap with low, then low += 1, mid += 1
# • If nums[mid] == 1, just move mid += 1
# • If nums[mid] == 2, swap with high, then high -= 1 (but do NOT move mid)