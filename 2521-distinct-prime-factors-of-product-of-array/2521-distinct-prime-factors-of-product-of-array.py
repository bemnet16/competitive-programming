class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        primes = set()
        
        for num in nums:
            
            divisor = 2
            
            while num > 1:
                while not num % divisor:
                    primes.add(divisor)
                    num //= divisor
                
                divisor += 1
        
        
        
        return len(primes)