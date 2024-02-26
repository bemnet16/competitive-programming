class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        nums = [i for i in range(1, (n + 1))]
        answer = []
        
        def backtrack(i, path):
            
            if len(path) == k:
                answer.append(path.copy())
                return
            
            if i >= n:
                return
            
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
            
            backtrack(i + 1, path)
        
        backtrack(0, [])
        return answer
        
        
        
        
        
#         answer = []
        
#         def backtrack(start, path):
            
#             if len(path) == k:
#                 answer.append(path.copy())
#                 return
            
#             for num in range(start, n + 1):
#                 path.append(num)
#                 backtrack(num + 1, path)
#                 path.pop()
            
#         backtrack(1, [])
#         return answer
        