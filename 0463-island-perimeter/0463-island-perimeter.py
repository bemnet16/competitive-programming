class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        VISITED = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        
        def inbound(row, col):
            
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))
        
        
        answer = 0
        def dfs(row, col):
            
            nonlocal answer
            
            if not grid[row][col]:
                answer += 1
                return
            
            
            VISITED[row][col] = True
            
            for row_change, col_change in DIRECTIONS:
                
                new_row = row + row_change
                new_col = col + col_change
                
                bounded = inbound(new_row, new_col)
                
                if bounded and not VISITED[new_row][new_col]:
                    dfs(new_row, new_col)
                
                elif not bounded:
                    answer += 1
        
        index = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    index = [row, col]
        

        if index: dfs(index[0], index[1])
        return answer
    
    
    
    
    
    
    
    
    
    
    