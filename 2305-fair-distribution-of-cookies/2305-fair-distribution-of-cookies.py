class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        if len(cookies) == k:
            return max(cookies)
        
        answer = float("inf")
        mx = float("-inf")
        
        def backtrack(index, distrib):
            
            nonlocal answer
            nonlocal mx
            
            if index >= len(cookies):
                answer = min(answer, mx)
                return
            
            if mx >= answer:
                return
            
            for person in range(k):
                distrib[person] += cookies[index]
                p_mx = mx
                mx = max(mx, distrib[person])
                backtrack(index + 1, distrib)
                distrib[person] -= cookies[index]
                mx = p_mx
                
            
        
        backtrack(0, [0] * k)
        return answer