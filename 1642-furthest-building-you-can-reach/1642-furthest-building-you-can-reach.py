class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        if len(heights) <= 1:
            return 0
        
        minHeap = []
        furthest = 0
        
        for i in range(1, len(heights)):
            
            diff = heights[i] - heights[i - 1]
            
            if diff <= 0:
                furthest += 1
                continue
            
            if ladders > 0:
                ladders -= 1
                heappush(minHeap, diff)
            
            elif minHeap and diff > minHeap[0]:
                if bricks - minHeap[0] < 0:
                    break
                else:
                    bricks -= heappop(minHeap)
                    heappush(minHeap, diff)
            
            elif bricks - diff < 0:
                break
            
            else:
                bricks -= diff
                
            furthest += 1
        
        
        return furthest
            
            