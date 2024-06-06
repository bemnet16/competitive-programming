class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        stk = []
        ans = 0
        
        for price in prices:
            
            if stk and stk[-1] < price:
                ans += price - stk.pop()
            
            stk.append(price)
        
        
        return ans
                