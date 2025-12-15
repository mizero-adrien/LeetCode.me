from typing import List
class Solution:
    def nextGreaterElement(self, nums1:List[int], nums2:List[int]) ->List[int]:
        stack = []               # monotonic decreasing stack
        next_greater = {}        # hashmap to store next greater for each element

        # Step 1: Build next greater map using stack
        for num in nums2:
            # While current num is greater than stack top → it is next greater
            while stack and num > stack[-1]:
                smaller = stack.pop()
                next_greater[smaller] = num
            stack.append(num)

        # Step 2: Elements remaining in the stack → no next greater
        while stack:
            next_greater[stack.pop()] = -1

        # Step 3: Build result for nums1 using hashmap
        return [next_greater[x] for x in nums1]