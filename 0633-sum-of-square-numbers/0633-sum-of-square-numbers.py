class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        sqrs = []
        
        i = 0
        while i * i <= c:
            sqrs.append(i * i)
            i += 1
        
        
        left, right = 0, len(sqrs) - 1
        while left <= right:
            if sqrs[left] + sqrs[right] > c:
                right -= 1
            
            elif sqrs[left] + sqrs[right] < c:
                left += 1
            
            else:
                return True
        
        return False