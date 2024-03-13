class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in rows[i]:
                    return False
                rows[i].add(board[i][j])
                
                if board[i][j] != '.' and board[i][j] in cols[j]:
                    return False
                cols[j].add(board[i][j])
        
        
        
        for i in range(3):
            for j in range(3):
                
                temp = set()
                
                for k in range(i * 3, i * 3 + 3):
                    for l in range(j * 3, j * 3 + 3):
                        
                        if board[k][l] != '.' and board[k][l] in temp:
                            return False
                        
                        temp.add(board[k][l])
        
        
        return True
        