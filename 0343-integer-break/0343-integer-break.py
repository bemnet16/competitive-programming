class Solution:
    def integerBreak(self, n: int) -> int:

        dp = [0, 0, 1, 2, 4, 6, 9]
        
        for _ in range(5, n):
            dp.append(dp[-3] * 3)
        
        return dp[n]