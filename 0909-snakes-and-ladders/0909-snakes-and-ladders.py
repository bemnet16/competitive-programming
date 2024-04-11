class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        n = len(board)

        start = 1
        lableLookup = defaultdict(list)
        for i in range(n):
            ele = [lable for lable in range(start, start + n)]
            if i % 2 == 0:
                lableLookup[n - i - 1] = ele.copy()
            else:
                lableLookup[n - i - 1] = ele[::-1].copy()
            start += n

        
        coordinateLookup = defaultdict(tuple)
        for i in range(n):
            for j in range(n):
                coordinateLookup[lableLookup[i][j]] = (i, j)



        level = [(n- 1, 0)]
        visited = {(n - 1, 0)}
        moves = 0

        ### use BFS approach to find the shorters move ###
        while level:

            next_level = []

            for row, col in level:

                if lableLookup[row][col] == (n ** 2):
                    return moves

                lable = lableLookup[row][col]

                for nxt in range(1, 7):

                    next_lable = lable + nxt

                    if next_lable <= (n * n) and coordinateLookup[next_lable] not in visited:
                    
                        r, c = coordinateLookup[next_lable]

                        visited.add((r, c))

                        if board[r][c] != -1:
                            r, c = coordinateLookup[board[r][c]]
                        
                        next_level.append((r, c))
            
            moves += 1
            level = next_level
        

        return -1
