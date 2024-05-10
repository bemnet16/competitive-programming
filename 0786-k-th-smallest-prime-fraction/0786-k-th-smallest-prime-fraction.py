class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
        heap = []
        
        for i in range(len(arr)):
            for j in range(len(arr)):
            
                if len(heap) < k:
                    heappush(heap, (-arr[i] / arr[j], (arr[i], arr[j])))

                else:
                    heappushpop(heap, (-arr[i]/arr[j], (arr[i], arr[j])))
        
        
        return heappop(heap)[1]
        