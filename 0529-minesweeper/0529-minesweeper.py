class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        
        DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        def inbound(row, col):
            return (0 <= row < len(board)) and (0 <= col < len(board[0]))
        
        
        def dfs(row, col):
            
            count = 0
            for row_change, col_change in DIRECTIONS:
                
                new_row = row + row_change
                new_col = col + col_change
                
                if inbound(new_row, new_col) and board[new_row][new_col] == "M":
                    count += 1
            
            if not count:
                board[row][col] = "B"
                for row_change, col_change in DIRECTIONS:
                
                    new_row = row + row_change
                    new_col = col + col_change

                    if inbound(new_row, new_col) and board[new_row][new_col] == "E":
                        dfs(new_row, new_col)
            
            else:
                board[row][col] = str(count)
             
            
        
        
        
        dfs(click[0], click[1])
        return board