class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        # to check overlapping easily sort by there start point
        points.sort(key = lambda x:x[0])
        
        # initialize with 1 since at least we need one arrow
        arrows = 1

        n = len(points)
        current = n - 1
        pointer = n - 1
        
        # helper function to check if two ballons are overlapping or not.
        def isOverLap(ballon_1, ballon_2):
            
            # start - end point for the two ballons
            x1, y1 = ballon_1
            x2, y2 = ballon_2
            
            if x1 <= x2 and x2 <= y1:
                return True
            
            if x2 <= y1 and y1 <= y2:
                return True
            
            return False
        


        for i in range((n - 1), -1, -1):
            
            if isOverLap(points[pointer], points[current]):
                pointer -= 1
            
            else:
                arrows += 1
                current = pointer
                pointer -= 1
        
        return arrows