class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        directions = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
        cur_x, cur_y = 0, 0
        visited = {(0, 0)}
        
        for d in path:
            
            to_x, to_y = directions[d]
            cur_x += to_x
            cur_y += to_y
            
            if (cur_x, cur_y) in visited:
                return True
            visited.add((cur_x, cur_y))
        
        return False
            
        