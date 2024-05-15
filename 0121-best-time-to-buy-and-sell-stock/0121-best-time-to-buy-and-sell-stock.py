class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = 0
        
        for i in range(len(prices) - 2, -1, -1):
            
            ans = max(ans, prices[i + 1] - prices[i])
            prices[i] = max(prices[i], prices[i + 1])
        
        
        return ans
