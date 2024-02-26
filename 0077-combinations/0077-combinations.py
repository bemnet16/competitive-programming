class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        answer = []
        
        def backtrack(start, path):
            
            if len(path) == k:
                answer.append(path.copy())
                return
            
            for num in range(start, n + 1):
                path.append(num)
                backtrack(num + 1, path)
                path.pop()
            
        backtrack(1, [])
        return answer
        