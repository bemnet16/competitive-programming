class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        answer = float("inf")
        
        def backtrack(index, distrib):
            nonlocal answer
            
            if index >= len(cookies):
                answer = min(answer, max(distrib))
                return
            
            if max(distrib) >= answer:
                return
            
            for person in range(k):
                distrib[person] += cookies[index]
                backtrack(index + 1, distrib)
                distrib[person] -= cookies[index]
            
        
        backtrack(0, [0] * k)
        return answer