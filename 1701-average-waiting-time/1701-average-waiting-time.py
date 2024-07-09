class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        cur = customers[0][0]
        waitings = 0
        
        for arrive_time, time_take in customers:
            
            cur = cur + time_take if cur >= arrive_time else arrive_time + time_take
            waitings += cur - arrive_time
        
        
        return waitings / len(customers)
            
        