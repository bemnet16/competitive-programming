class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.answer = set()
        
        def backtrack(idx, sub, sm):
            
            if sm == target:
                temp = sub.copy()
                temp.sort()
                if tuple(temp) not in self.answer:
                    self.answer.add(tuple(temp))
                return
            
            if sm > target:
                return
            
            for i in range(len(candidates)):
                sub.append(candidates[i])
                sm += candidates[i]
                backtrack(i + 1, sub, sm)
                sm -= sub.pop()
            
        backtrack(0, [], 0)
        return self.answer