class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        answer = []
        
        def backtrack(idx, sub):
            
            if idx >= len(nums):
                temp = sub.copy()
                temp.sort()
                if temp not in answer:
                    answer.append(temp)
                return
            
            
            sub.append(nums[idx])
            backtrack(idx + 1, sub)
            sub.pop()
            
            backtrack(idx + 1, sub)
        
        backtrack(0, [])
        return answer
        