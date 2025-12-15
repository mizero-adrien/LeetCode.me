from typing import List
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n

        for i in range(n):        # target box
            ops = 0
            for j in range(n):    # check every other box
                if boxes[j] == '1':
                    ops += abs(i - j)   # distance = moves needed
            answer[i] = ops

        return answer