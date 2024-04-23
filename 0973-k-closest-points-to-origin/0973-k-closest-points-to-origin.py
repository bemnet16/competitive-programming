import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []
        
        def calcDistance(x, y):
            
            return ((x ** 2) + (y ** 2))
            
        
        dis = defaultdict(list)
        
        for i, co in enumerate(points):
            
            x, y = co
            
            distance = calcDistance(x, y)
            dis[distance].append([x, y])
            heappush(minHeap, distance)
            
        
        closest = []
        while k > 0:
            mn = dis[heappop(minHeap)]
            while k > 0 and mn:
                closest.append(mn.pop())
                k -= 1
            
        
        return closest
        