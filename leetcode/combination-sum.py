class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        answer = []
        
        def backtrack(idx, sub):
            
            s_sub = sum(sub)
            
            if s_sub == target:
                temp = sub.copy()
                temp.sort()
                if temp not in answer:
                    answer.append(temp)
                return
            
            if s_sub > target:
                return
            
            for i in range(len(candidates)):
                sub.append(candidates[i])
                backtrack(i + 1, sub)
                sub.pop()
            
        backtrack(0, [])
        return answer