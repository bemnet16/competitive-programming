class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        
        maxHeap = []
        for pile in piles:
            heappush(maxHeap, -pile)
        
        
        for _ in range(k):
            
            maxPile = -heappop(maxHeap)
            heappush(maxHeap, -(maxPile - (maxPile // 2)))
        
        
        
        return -sum(maxHeap)