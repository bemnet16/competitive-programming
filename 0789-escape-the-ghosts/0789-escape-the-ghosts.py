class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        
        tx, ty = target
        min_move = abs(tx) + abs(ty)
        
        for gx, gy in ghosts:
            if abs(gx - tx) + abs(gy - ty) <= min_move:
                return False
        return True