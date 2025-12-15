from collections import deque

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        queue = deque()

        # Count frequency and track first appearance using queue
        for i, ch in enumerate(s):
            freq[ch] = freq.get(ch, 0) + 1
            queue.append((ch, i))

            # Ensure queue front is always unique
            while queue and freq[queue[0][0]] > 1:
                queue.popleft()

        # If queue not empty, front has the first unique char
        return queue[0][1] if queue else -1
