class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        for i in range(1, len(grid[0])):
            grid[0][i] += grid[0][i - 1]
            grid[1][len(grid[0]) - i - 1] += grid[1][len(grid[0]) - i]
        
        
        
        ans = float('inf')
        
        for i in range(len(grid[0])):
            ans = min(ans, max((grid[1][0] - grid[1][i]), (grid[0][-1] - grid[0][i])))
        
        
        return ans
        