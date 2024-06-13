class Solution:
    
    def dfs(self, n, k, rootVal):
        if n == 1:
            return rootVal
        
        totalNodes = 1 << (n - 1)
        
        if k <= totalNodes / 2:
            if rootVal == 0:
                return self.dfs(n - 1, k, 0)
            else:
                return self.dfs(n - 1, k, 1)
        else:
            if rootVal == 0:
                return self.dfs(n - 1, k - (totalNodes / 2), 1)
            else:
                return self.dfs(n - 1, k - (totalNodes / 2), 0)
    
    
    def kthGrammar(self, n: int, k: int) -> int:
        
        return self.dfs(n, k, 0)
