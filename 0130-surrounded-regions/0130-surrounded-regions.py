class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        m, n = len(board), len(board[0])
        
        DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        def inbound(row, col):
            return (0 <= row < m) and (0 <= col < n)
        
        
        def dfs(row , col):
            
            board[row][col] = "T"
            
            for row_change, col_change in DIRECTIONS:
                
                new_row = row + row_change
                new_col = col + col_change
                
                if inbound(new_row, new_col) and board[new_row][new_col] == "O":
                    dfs(new_row, new_col)
            
            
        
        
        border1 = [(0, n), (m - 1, n)]
        border2 = [(0, m - 1), (n - 1, m - 1)]
        
        for i in range(2):
            
            for b1 in range(border1[i][1]):
                if board[border1[i][0]][b1] == "O":
                    dfs(border1[i][0], b1)
            
            
            for b2 in range(1, border2[i][1]):
                if board[b2][border2[i][0]] == "O":
                    dfs(b2, border2[i][0])
        
        
        
        for row in range(m):
            for col in range(n):
                if board[row][col] == "O":
                    board[row][col] = "X"
                
                elif board[row][col] == "T":
                    board[row][col] = "O"
        
        
        return board
                    
                    
                
                
                
                