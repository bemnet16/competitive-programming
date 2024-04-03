class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        
        limit = [[0, 0] for _ in range(n)]
        
        for i in range(n):
            
            if (i + 1) < n:
                limit[i + 1][0] = max(limit[i][0], height[i])
            
            if (n - i - 2) > 0:
                limit[n - i - 2][1] = max(height[n - i - 1], limit[n - i - 1][1])
        
        
        rainTrap = 0
        for i in range(1, n - 1):
            
            water = min(limit[i]) - height[i]
            
            if water > 0:
                rainTrap += water
        
        
        return rainTrap
                