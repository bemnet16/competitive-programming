class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        # there is no need to go to back track if the length of cookies and the number of k are equal
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
                
                restore_mx = mx
                mx = max(mx, distrib[person])
                
                backtrack(index + 1, distrib)
                distrib[person] -= cookies[index]
                
                # reset the maximum to the previous maximum value after it return from backtracking
                mx = restore_mx
                
            
        
        backtrack(0, [0] * k)
        return answer