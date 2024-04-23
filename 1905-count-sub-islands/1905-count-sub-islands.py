class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        def inbound(row, col):
            return (0 <= row < len(grid1)) and (0 <= col < len(grid1[0]))
        
        
        positions = []
        
        def dfs(row, col):
            
            nonlocal positions
            
            grid2[row][col] = 0
            
            for row_change, col_change in DIRECTIONS:
                
                new_row = row + row_change
                new_col = col + col_change
                
                if inbound(new_row, new_col) and grid2[new_row][new_col] == 1:
                    positions.append((new_row, new_col))
                    dfs(new_row, new_col)
        
        
        def check(positions):
            for row, col in positions:
                if grid1[row][col] != 1:
                    return False
            return True
        
        
        subIsland = 0
    
        for row in range(len(grid1)):
            for col in range(len(grid1[0])):
                
                if grid2[row][col] == 1:
                    
                    positions.append((row, col))
                    dfs(row, col)
                    
                    if check(positions):
                        subIsland += 1
                        
                    positions = []
        
        
        return subIsland
        