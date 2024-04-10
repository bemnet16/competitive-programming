class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        def inbound(row, col):
            
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))
        
        
        perimeter = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if not grid[row][col]:
                    continue
                
                for row_chg, col_chg in DIRECTIONS:
                    new_row = row + row_chg
                    new_col = col + col_chg
                    
                    if inbound(new_row, new_col) and not grid[new_row][new_col]:
                        perimeter += 1
                    
                    elif not inbound(new_row, new_col):
                        perimeter += 1
        
        
        return perimeter