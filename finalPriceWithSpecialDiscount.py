from typing import List
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        answer = [0] * n
        
        for i in range(n):
            discount = 0
            # Check for the first price to the right that is <= prices[i]
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    discount = prices[j]
                    break  # stop at first valid discount
            answer[i] = prices[i] - discount
        
        return answer