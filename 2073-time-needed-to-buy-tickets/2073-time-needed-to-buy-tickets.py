class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        
        time_taken = 0
        
        for i in range(k + 1):
            
            if tickets[i] >= tickets[k]:
                time_taken += tickets[k]
            
            else:
                time_taken += tickets[i]
        
        
        for i in range((k + 1), len(tickets)):
            
            if tickets[i] >= tickets[k] - 1:
                time_taken += (tickets[k] - 1)
            
            else:
                time_taken += tickets[i]
        
        
        return time_taken