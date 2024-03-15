class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        grid = [["" for _ in range(n)] for _ in range(m)]
        
        
        for row, col in guards:
            grid[row][col] = "G"
        
        for row, col in walls:
            grid[row][col] = "W"
        
        
        for row in range(m):
            
            rowf_guarded = False
            
            for col in range(n):
                
                grid_val = grid[row][col]
                
                if grid_val == "G":
                    rowf_guarded = True
                
                elif grid_val == "W":
                    rowf_guarded = False
                
                elif grid_val == "" and not rowf_guarded:
                    grid[row][col] = "U"
                
                elif rowf_guarded:
                    grid[row][col] = "g"
                    
                    
        for row in range(m):
            
            rowb_guarded = False
            
            for col in range(n):
                
                grid_val = grid[row][n - col - 1]
                
                if grid_val == "G":
                    rowb_guarded = True
                
                elif grid_val == "W":
                    rowb_guarded = False
                
                elif grid_val == "" and not rowb_guarded:
                    grid[row][n - col - 1] = "U"
                
                elif rowb_guarded:
                    grid[row][n - col - 1] = "g"
                    
        for col in range(n):
            
            colf_guarded = False
            
            for row in range(m):
                
                grid_val = grid[row][col]
                
                if grid_val == "G":
                    colf_guarded = True
                
                elif grid_val == "W":
                    colf_guarded = False
                
                elif grid_val == "" and not colf_guarded:
                    grid[row][col] = "U"
                
                elif colf_guarded:
                    grid[row][col] = "g"
                    
                    
        for col in range(n):
            
            colb_guarded = False
            
            for row in range(m):   
                
                grid_val = grid[m - row - 1][col]
                
                if grid_val == "G":
                    colb_guarded = True
                
                elif grid_val == "W":
                    colb_guarded = False
                
                elif grid_val == "" and not colb_guarded:
                    grid[m - row - 1][col] = "U"
                
                elif colb_guarded:
                    grid[m - row - 1][col] = "g"
                
                
        tot_unguarded = 0
        
        for row in grid:
            for col in row:
                tot_unguarded += (col == "U")

                
        return tot_unguarded
                
                
                    
                
                