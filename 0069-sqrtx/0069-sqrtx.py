class Solution(object):
    def mySqrt(self, x):
        res = 0
        while (res * res) <= x:
            res += 1
        
        return res - 1