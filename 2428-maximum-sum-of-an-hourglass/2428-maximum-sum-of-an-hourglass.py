class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        answer = float("-inf")
        
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                
                row1 = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
                mid = grid[i + 1][j + 1]
                row3 = grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
                
                answer = max(answer, (row1 + mid + row3))
                
                
                
        return answer