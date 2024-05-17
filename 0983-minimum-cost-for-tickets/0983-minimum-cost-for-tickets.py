class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        d_cost = [1, 7, 30]
        
        cache = {}
        days_set = set(days)
        
        def dp(day):
            
            if day > days[-1]:
                return 0
            
            if day not in days_set:
                return dp(day + 1)
            
            if day in cache:
                return cache[day]
            
            
            day_1 = costs[0] + dp(day + 1)
            day_2 = costs[1] + dp(day + 7)
            day_3 = costs[2] + dp(day + 30)
            
            cache[day] = min(day_1, day_2, day_3)
            
            return cache[day]
        
        
        return dp(1)
            
            