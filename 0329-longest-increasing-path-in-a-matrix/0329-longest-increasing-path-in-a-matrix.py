class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        
        DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        indegree = [[0 for _ in range(n)] for _ in range(m)]
        
        def inbound(row, col):
            return (0 <= row < m) and (0 <= col < n)
        
        for row in range(m):
            for col in range(n):
                
                for row_chg, col_chg in DIRECTIONS:
                    new_row = row + row_chg
                    new_col = col + col_chg
                    
                    if inbound(new_row, new_col) and matrix[row][col] > matrix[new_row][new_col]:
                        indegree[row][col] += 1
                        
        
        
        queue = deque()
        for row in range(m):
            for col in range(n):
                if indegree[row][col] == 0:
                    queue.append((row, col))
        
        
        long_path = 0
        while queue:
            
            for i in range(len(queue)):
                
                row, col = queue.popleft()
                for row_chg, col_chg in DIRECTIONS:
                    new_row = row + row_chg
                    new_col = col + col_chg
                    
                    if inbound(new_row, new_col) and matrix[row][col] < matrix[new_row][new_col]:
                        indegree[new_row][new_col] -= 1
                        if indegree[new_row][new_col] == 0:
                            queue.append((new_row, new_col))
            
            long_path += 1
        
        
        return long_path
                    

        ### DP approach ###
        
#         cache = {}
        
#         def inbound(row, col):
#             return (0 <= row < len(matrix)) and (0 <= col < len(matrix[0]))
        
#         def dp(row, col):
            
#             if not inbound(row, col):
#                 return 0
            
#             if (row, col) in cache:
#                 return cache[(row, col)]
            
            
#             left = 1
#             if inbound(row, col + 1) and matrix[row][col] < matrix[row][col + 1]:
#                 left = 1 + dp(row, col + 1)
                
#             right = 1
#             if inbound(row, col - 1) and matrix[row][col] < matrix[row][col - 1]:
#                 right = 1 + dp(row, col - 1)
                
#             up = 1
#             if inbound(row - 1, col) and matrix[row][col] < matrix[row - 1][col]:
#                 up = 1 + dp(row - 1, col)
                
#             down = 1
#             if inbound(row + 1, col) and matrix[row][col] < matrix[row + 1][col]:
#                 down = 1 + dp(row + 1, col)
            
            
#             cache[(row, col)] = max(left, right, up, down)
            
#             return cache[(row, col)]
        
        
        
#         long_path = 1
#         for row in range(len(matrix)):
#             for col in range(len(matrix[0])):
#                 long_path = max(long_path, dp(row, col))
                
#         return long_path
            
        