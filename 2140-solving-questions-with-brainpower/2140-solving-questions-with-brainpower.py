class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        n = len(questions)
        dp = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            
            point, brain_power = questions[i]
            
            next_question = min(n, i + brain_power + 1)
            dp[i] = max(dp[i + 1], point + dp[next_question])
        
        
        return dp[0]
            
        
        
        
        
#         cache = defaultdict(int)
        
#         def dp(i, cur):
            
#             if i in cache:
#                 return cache[i]
            
#             temp = 0
#             for j in range(i + questions[i][1] + 1, len(questions)):
#                 temp = max(temp, dp(j, cur + questions[j][0]))
            
#             cache[i] = questions[i][0] + temp
            
#             return cache[i]
        
        
#         ans = 0
#         for i in range(len(questions)):
#             ans = max(ans, dp(i, questions[i][0]))
        
#         return ans
        