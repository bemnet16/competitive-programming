class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        mn = min(nums)
        mx = max(nums)
        
        def gcd(a, b):
            
            if a % b == 0:
                return b
            
            return gcd(b, a % b)
        
        return gcd(mn, mx)
        