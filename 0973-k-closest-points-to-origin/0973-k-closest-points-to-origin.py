import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def calcDistance(x, y):
            return math.sqrt((x ** 2) + (y ** 2))
        
        for point in range(len(points)):
            
            x, y = points[point]
            distance = calcDistance(x, y)
            points[point].append(distance)
        
        points.sort(key=lambda x:x[2])
        
        for point in range(k):
            points[point].pop()
        
        return points[:k]
        
        
        
#         minHeap = []
        
#         def calcDistance(x, y):
            
#             return ((x ** 2) + (y ** 2))
            
        
#         dis = defaultdict(list)
        
#         for i, co in enumerate(points):
            
#             x, y = co
            
#             distance = calcDistance(x, y)
#             dis[distance].append([x, y])
#             heappush(minHeap, distance)
            
        
#         closest = []
#         while k > 0:
#             mn = dis[heappop(minHeap)]
#             while k > 0 and mn:
#                 closest.append(mn.pop())
#                 k -= 1
            
        
#         return closest
        