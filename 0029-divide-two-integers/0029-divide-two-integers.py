class Solution(object):
    def divide(self, dividend, divisor):
        
        if dividend == 0: return 0
        
        neg = False
        if (dividend < 0 and divisor > 0 ) or (dividend > 0 and divisor < 0 ): neg = True
            
        dividend = abs(dividend)
        divisor = abs(divisor)
            
#         res = 0
#         while dividend >= divisor:
#             dividend -= divisor
#             res += 1
        
        res = dividend // divisor
    
        if neg:
            res = -res
        
        
        return min(max(-2147483648, res), 2147483647)
        
        
            