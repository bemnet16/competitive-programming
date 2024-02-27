class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        answer = []
        
        def backtrack(idx, sub, sm):
            
            if sm == target:
                temp = sub.copy()
                temp.sort()
                if temp not in answer:
                    answer.append(temp)
                return
            
            if sm > target:
                return
            
            for i in range(len(candidates)):
                sub.append(candidates[i])
                sm += candidates[i]
                backtrack(i + 1, sub, sm)
                sm -= sub.pop()
            
        backtrack(0, [], 0)
        return answer