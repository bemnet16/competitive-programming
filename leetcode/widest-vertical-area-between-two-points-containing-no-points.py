class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        points.sort()
        widest_area = float("-inf")

        for i in range(1, len(points)):
            
            width = points[i][0] - points[i - 1][0]
            widest_area = max(widest_area, width)
            
            
        
        return widest_area