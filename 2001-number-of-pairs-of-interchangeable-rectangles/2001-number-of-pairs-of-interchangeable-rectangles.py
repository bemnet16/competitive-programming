class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        
        def get_gcf(a, b):
            if b == 0:
                return a
            return get_gcf(b, (a % b))
        
        
        
        counts = defaultdict(int)
        ans = 0
        
        for i in range(len(rectangles) - 1, -1, -1):
            
            width, height = rectangles[i]
            gcf = get_gcf(width, height)
            
            ans += counts[(width // gcf, height // gcf)]
            counts[(width // gcf, height // gcf)] += 1
        
        
        return ans
            
            
        