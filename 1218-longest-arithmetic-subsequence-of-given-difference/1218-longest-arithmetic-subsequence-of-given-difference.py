class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        dp = defaultdict(int)
        longest = 1
        
        for num in arr:
            dp[num] = dp[num - difference] + 1
            longest = max(longest, dp[num])
        
        
        return longest