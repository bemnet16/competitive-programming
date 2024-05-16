class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cache = {}
        
        def dp(i):
            
            if i >= len(cost):
                return 0
            
            if i in cache:
                return cache[i]
            
            climb_one = dp(i + 1) + cost[i]
            climb_two = dp(i + 2) + cost[i]
            
            cache[i] = min(climb_one, climb_two)
            
            return cache[i]
        
        
        return min(dp(0), dp(1))
        