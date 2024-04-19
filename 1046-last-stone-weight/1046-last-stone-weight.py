class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-stone for stone in stones]
        heapify(stones)
        
        while len(stones) > 1:
            
            y = heappop(stones)
            x = heappop(stones)
            
            if x != y:
                heappush(stones, y - x)
        
        
        if stones:
            return -stones[0]
        
        return 0
        
        