class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        cache = {}
        
        def dp(i, buy):
            
            if i >= len(prices):
                return 0
            
            if (i, buy) in cache:
                return cache[(i, buy)]
            
            notbuy = dp(i + 1, buy)
            
            if buy:
                profit = dp(i + 1, not buy) - prices[i]
            
            else:
                profit = dp(i + 1, not buy) + (prices[i] - fee)
            
            cache[(i, buy)] = max(profit, notbuy)
            
            return cache[(i, buy)]
        
        
        return dp(0, True)
        