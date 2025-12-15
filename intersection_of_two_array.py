from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int])->List[int]:
        return list(set(nums1) & set(nums2))
       #set for removing duplicates and & for intersection
    
sol = Solution()
print(sol.intersection([1,2,2,1], [2,2]))