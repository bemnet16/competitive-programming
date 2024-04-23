from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        def inbound(row, col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))
        
        queue = []
        fresh = 0
        minutes = -1
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col))
                
                elif grid[row][col] == 1:
                    fresh += 1
        
        if not fresh:
            return 0
        
        
        while queue:
            
            nx_queue = []
            
            for row, col in queue:
                
                for row_change, col_change in DIRECTIONS:
                    
                    new_row = row + row_change
                    new_col = col + col_change
                    
                    if inbound(new_row, new_col) and grid[new_row][new_col] == 1:
                        
                        nx_queue.append((new_row, new_col))
                        grid[new_row][new_col] = 2
                        fresh -= 1
            
            minutes += 1
            if nx_queue:
                queue = nx_queue
            else:
                queue = []
        
        
        return minutes if not fresh else -1
                
            
        
        