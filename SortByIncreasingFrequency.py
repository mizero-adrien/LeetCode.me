from typing import List
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # brute-force frequency count
        freq = []
        for x in nums:
            count = 0
            for y in nums:
                if y == x:
                    count += 1
            freq.append([x, count])  # store value + its frequency

        # brute-force bubble sort using the rules
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                # rule 1: sort by frequency ascending
                if freq[i][1] > freq[j][1]:
                    freq[i], freq[j] = freq[j], freq[i]
                # rule 2: if frequency same → sort by value descending
                elif freq[i][1] == freq[j][1] and freq[i][0] < freq[j][0]:
                    freq[i], freq[j] = freq[j], freq[i]

        # build result
        result = [val for val, f in freq]
        return result
       