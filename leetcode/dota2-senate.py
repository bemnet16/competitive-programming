from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        n = len(senate)
        
        dire_queue = deque()
        rad_queue = deque()
        
        
        for senator in range(len(senate)):
            
            if senate[senator] == "D":
                dire_queue.append(senator)
            
            else:
                rad_queue.append(senator)
        
        while dire_queue and rad_queue:
            
            senator_D = dire_queue[0]
            senator_R = rad_queue[0]
            
            rad_queue.popleft()
            dire_queue.popleft()
            
            if senator_D < senator_R:
                dire_queue.append(n)
            
            else:
                rad_queue.append(n)
            
            n += 1
        
        if dire_queue:
            return "Dire"
        
        return "Radiant"
        
