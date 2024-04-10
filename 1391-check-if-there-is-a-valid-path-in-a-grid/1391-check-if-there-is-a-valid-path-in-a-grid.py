class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        RIGHT = (0, 1)
        LEFT = (0, -1)
        UP = (-1, 0)
        DOWN = (1, 0)
        
        DIRECTIONS = [RIGHT, LEFT, UP, DOWN]
        
        VALID = {
            1: {(LEFT, 1), (LEFT, 4), (LEFT, 6), (RIGHT, 1), (RIGHT, 3), (RIGHT, 5)},
            2: {(UP, 2), (UP, 4), (UP, 3), (DOWN, 2), (DOWN, 5), (DOWN, 6)},
            3: {(LEFT, 1), (LEFT, 4), (LEFT, 6), (DOWN, 2), (DOWN, 5), (DOWN, 6)},
            4: {(RIGHT, 1), (RIGHT, 3), (RIGHT, 5), (DOWN, 2), (DOWN, 5), (DOWN, 6)},
            5: {(LEFT, 1), (LEFT, 4), (LEFT, 6), (UP, 2), (UP, 3), (UP, 4)},
            6: {(RIGHT, 1), (RIGHT, 3), (RIGHT, 5), (UP, 2), (UP, 3), (UP, 4)}
        }
        
        VISITED = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        
        def dfs(row, col):
            
            if (row == (len(grid) - 1) ) and (col == (len(grid[0]) - 1)):
                return True
            
            
            VISITED[row][col] = True
            
            for row_change, col_change in DIRECTIONS:
                
                new_row = row + row_change
                new_col = col + col_change
                
                if inbound(new_row, new_col) and not VISITED[new_row][new_col]:
                    if ((row_change, col_change), grid[new_row][new_col]) in VALID[grid[row][col]]:
                        if dfs(new_row, new_col):
                            return True
            
            return False
            
            
        return dfs(0, 0)