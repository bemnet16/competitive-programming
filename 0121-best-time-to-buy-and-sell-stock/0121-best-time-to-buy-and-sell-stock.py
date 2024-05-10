class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = 0
        heap = [prices[-1]]
        
        for i in range(len(prices) - 2, -1, -1):
            
            ans = max(ans, (heap[0] - prices[i]))
            heappushpop(heap, prices[i])
            
            
        return ans
    
    
        
#         ans = 0
#         stk = []
        
#         i = 0
#         while i < len(prices):
            
#             while stk and prices[i] < stk[-1]:
#                 stk.pop()
            
#             while i < len(prices) and stk and stk[-1] <= prices[i]:
#                 ans = max(ans, (prices[i] - stk[-1]))
#                 i += 1
            
#             if i < len(prices):
#                 stk.append(prices[i])
        
#         return ans
        
        
        
#         def dp(i, profit, state):
            
#             nonlocal ans
            
#             if i >= len(prices):
#                 return
            
            
#             if state == "N":
#                 dp(i + 1, profit - prices[i], "B")
#                 dp(i + 1, profit, "N")
            
            
#             elif state == "B":
#                 ans = max(ans, (profit + prices[i]))
#                 dp(i + 1, profit, "B")
            
            
            
            
        
        
#         ans = 0
#         dp(0, 0, "N")
#         return ans
            

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            