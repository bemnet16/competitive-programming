class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        gaps = defaultdict(int)
        max_gap = 0
        
        for w in wall:
            
            cur = 0
            for i in range(len(w) - 1):
                cur += w[i]
                gaps[cur] += 1
                max_gap = max(max_gap, gaps[cur])
        
        
        return len(wall) - max_gap
        