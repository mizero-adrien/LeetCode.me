from collections import deque
class RecentCounter:

    def __init__(self):
        self.q = deque() #queue to store the ping items        

    def ping(self, t: int) -> int:
        self.q.append(t) # add new request  

        #removing the request that is greater than 3000
        while self.q[0] < t-3000:
            self.q.popleft()

        return len(self.q)   #count of valid request



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)