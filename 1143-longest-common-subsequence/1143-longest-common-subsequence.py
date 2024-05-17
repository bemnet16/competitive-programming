class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        ### Bottom - Up Approach ###
        
        dp = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]
        
        for row in range(len(text2) - 1, -1, -1):
            for col in range(len(text1) - 1, -1, -1):
                
                if text1[col] == text2[row]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                
                else:
                    dp[row][col] = max(dp[row][col + 1], dp[row + 1][col])
        
        return dp[0][0]
        
        
        
        ### Top - Down Approach ###
        
        memo = {}
        
        def dp(i, j):
            
            if (i >= len(text1)) or (j >= len(text2)):
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            if text1[i] == text2[j]:
                cur = 1 + dp(i + 1, j + 1)
            
            else:
                cur_l = dp(i + 1, j)
                cur_r = dp(i, j + 1)
                
                cur = max(cur_l, cur_r)
            
            memo[(i, j)] = cur
            return memo[(i, j)]
        
        
        return dp(0, 0)