class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        def inbound(row, col):
            return (0 <= row < len(board)) and (0 <= col < len(board[0]))
        
        
        
        def dfs(vis, row, col, i):
            
            if i >= len(word):
                return True
            
            for row_chg, col_chg in DIRECTIONS:
                new_row = row + row_chg
                new_col = col + col_chg
                
                if (new_row, new_col) not in vis and inbound(new_row, new_col) and board[new_row][new_col] == word[i]:
                    vis.add((new_row, new_col))
                    if dfs(vis, new_row, new_col, i + 1):
                        return True
                    vis.remove((new_row, new_col))
            return False
            
        
        
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if dfs({(row, col)}, row, col, 1):
                        return True
        
        return False
                
        
        