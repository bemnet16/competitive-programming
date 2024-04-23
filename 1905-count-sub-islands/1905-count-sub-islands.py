class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        def inbound(row, col):
            return (0 <= row < len(grid1)) and (0 <= col < len(grid1[0]))
        
        
        rc = []
        def dfs(row, col):
            
            nonlocal rc
            
            grid2[row][col] = 0
            
            for row_change, col_change in DIRECTIONS:
                
                new_row = row + row_change
                new_col = col + col_change
                
                if inbound(new_row, new_col) and grid2[new_row][new_col] == 1:
                    rc.append((new_row, new_col))
                    dfs(new_row, new_col)
        
        
        def check(rc):
            
            for r, c in rc:
                if grid1[r][c] != 1:
                    return False
            return True
        
        
        subIsland = 0
    
        for row in range(len(grid1)):
            for col in range(len(grid1[0])):
                if grid2[row][col] == 1:
                    rc.append((row, col))
                    dfs(row, col)
                    if check(rc):
                        subIsland += 1
                    rc = []
        
        
        return subIsland
        