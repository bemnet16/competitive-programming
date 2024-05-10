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
        
        
        
#         cache = [None] * len(prices)
#         cache[-1] = 0
        
#         def dp(i):
            
#             nonlocal ans
            
#             if i >= len(prices):
#                 return 0
            
#             mx = 0
#             for j in range(i + 1, len(prices)):
#                 if cache[j] != None:
#                     dp_j = cache[j]
#                 else:
#                     dp_j = dp(j)
#                     cache[j] = dp_j
                    
#                 mx = max(mx, prices[j] - prices[i]) 
            
#             ans = max(ans, mx)
#             return prices[i]
        
#         ans = 0
#         # for stock in range(len(prices)):
#         #     if prices[stock] != 0 and prices[stock] > ans:
#         dp(0)
            
        
#         return ans