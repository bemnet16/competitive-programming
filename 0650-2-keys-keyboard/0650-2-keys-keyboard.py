class Solution:
    def minSteps(self, n: int) -> int:
        
        if n <= 1: return 0
        
        cache = defaultdict(int)
        
        def dp(s_len, p_len):
            
            if (s_len, p_len) in cache:
                return cache[(s_len, p_len)]
            
            if s_len == n:
                return 0
            
            if s_len > n:
                return float("inf")
            
            res_1 = 1 + dp(s_len + p_len, p_len)
            res_2 = 2 + dp(2 * s_len, s_len)
            
            cache[(s_len, p_len)] = min(res_1, res_2)
            return cache[(s_len, p_len)]
        
        
        return 1 + dp(1, 1)
        