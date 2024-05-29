class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        if n <= 1: return n
        
        
        def dp(i):
            
            nonlocal ans
            
            if i <= 1:
                return i
            
            if ans[i] != -1:
                return ans[i]
            
            if i % 2 == 0:
                res = dp(i // 2)
            
            else:
                res = dp(i // 2) + dp((i // 2 )+ 1)
            
            ans[i] = res
            return ans[i]
        
        
        ans = [-1] * (n + 1)
        ans[0] = 0
        ans[1] = 1
        
        for i in range(n + 1):
            dp(i)
            
        return max(ans)
        