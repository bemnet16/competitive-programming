import math

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        
        def canMake(num):
            que1 = num - (num // divisor1)
            que2 = num - (num // divisor2)
            que_12 = num - (num // math.lcm(divisor1, divisor2))
            
            return que1 >= uniqueCnt1 and que2 >= uniqueCnt2 and que_12 >= (uniqueCnt1 + uniqueCnt2)
        
        
        low = 0
        high = 10 ** 10
        
        while low <= high:
            
            mid = low + (high - low) // 2
            
            if canMake(mid):
                high = mid - 1
            
            else:
                low = mid + 1
        
        
        return low