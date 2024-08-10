class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        
        land = [[0 for _ in range(len(grid) * 3)] for _ in range(len(grid)* 3)]

        # change slash to 0's and 1's
        # then it is easy. just traverse and count connected 0's
        for i in range(len(grid)):
            for j in range(len(grid)):
                
                r, c = (i * 3), (j * 3)
                
                if grid[i][j] == '/':
                    land[r][c + 2], land[r + 1][c + 1], land[r + 2][c] = 1, 1, 1
                elif grid[i][j] == '\\':
                    land[r][c], land[r + 1][c + 1], land[r + 2][c + 2] = 1, 1, 1
        
        
        DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        
        def inbound(row, col):
            return (0 <= row < len(land)) and (0 <= col < len(land))
        
        
        def dfs(row, col):
            
            land[row][col] = 1
            for row_change, col_change in DIRECTIONS:
                
                new_row = row + row_change
                new_col = col + col_change
                
                if inbound(new_row, new_col) and land[new_row][new_col] == 0:
                    dfs(new_row, new_col)
            
            
        regions = 0
        for row in range(len(land)):
            for col in range(len(land[0])):
                if land[row][col] == 0:
                    regions += 1
                    dfs(row, col)
         
        return regions
        
        