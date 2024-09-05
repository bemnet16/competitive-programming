class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        
        m, sum_m = len(rolls), sum(rolls)
        sum_n = ((n + m) * mean) - sum_m
        
        if sum_n <= 0:
            return []
        
        
        quotient = sum_n // n
        reminder = sum_n % n
        
        if quotient <= 0 or quotient > 6 or (quotient == 6 and reminder > 0):
            return []
        
        ans = [quotient] * n
        for i in range(reminder):
            ans[i] += 1
        
        return ans
        
        
        
        