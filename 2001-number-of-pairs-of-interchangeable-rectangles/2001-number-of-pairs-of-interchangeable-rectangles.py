class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        
        counts = defaultdict(int)
        ans = 0
        
        for i in range(len(rectangles) - 1, -1, -1):
            
            width, height = rectangles[i]
            ans += counts[(width / height)]
            counts[(width /height)] += 1
        
        
        return ans
            
            
        