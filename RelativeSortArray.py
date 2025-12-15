from typing import List
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Step 1: Map each value in arr2 to its index
        order = {value: i for i, value in enumerate(arr2)}

        # Step 2: Custom sorting rule
        def sort_key(x):
            # If x is in arr2, return its index
            if x in order:
                return (0, order[x])
            # If x not in arr2, put it later but sorted
            return (1, x)

        # Step 3: Sort using our custom key
        return sorted(arr1, key=sort_key)