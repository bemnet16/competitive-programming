class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        def count(n):
            if n == 1:
                return 5
            
            if n == 2:
                return 20
            
            if n % 2 == 0:
                if (n // 2) % 2 == 0:
                    return pow(count(n // 2), 2, MOD)
                else:
                    return (pow(count((n // 2) - 1), 2, MOD) * count(2)) % MOD
            else:
                return( pow(count(n // 2), 2, MOD) * (5 if (n // 2) % 2 == 0 else 4)) % MOD
        
        return count(n)
