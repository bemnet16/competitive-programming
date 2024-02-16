from collections import deque

class RecentCounter:

    def __init__(self):
        self.recentCounter = 0
        self.deque = deque()
        

    def ping(self, t: int) -> int:
        self.deque.append(t)
        self.recentCounter += 1
        
        while (self.deque[0] < (t - 3000)):
            self.deque.popleft()
            self.recentCounter -= 1
        
        return self.recentCounter
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)