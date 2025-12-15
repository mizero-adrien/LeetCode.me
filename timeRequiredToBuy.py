from typing import List
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        target = tickets[k]

        for i in range(len(tickets)):
            if i <= k:
                time += min(tickets[i], target)
            else:
                time += min(tickets[i], target - 1)

        return time
sol = Solution()
print(sol.timeRequiredToBuy([2,1,2],2))