class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        ans = set()
        
        def backtrack(target, idx, comb):
            
            if target < 0:
                return
            
            if target == 0:
                ans.add(tuple(comb.copy()))
            
            for i in range(idx, len(candidates)):
                
                if i > idx and candidates[i - 1] == candidates[i]:
                    continue
                
                val = candidates[i]
                
                backtrack(target - val, i + 1, comb + [val])
        
        
        backtrack(target, 0, [])
        return ans
                
                