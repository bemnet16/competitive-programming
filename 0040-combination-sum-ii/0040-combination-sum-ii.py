class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        ans = []
        
        def backtrack(_sum, idx, comb):
            
            if _sum > target:
                return
            
            if target == _sum:
                ans.append(comb.copy())
                return
            
            
            for i in range(idx, len(candidates)):
                
                if i > idx and candidates[i - 1] == candidates[i]:
                    continue
                
                val = candidates[i]
                comb.append(val)
                backtrack(_sum + val, i + 1, comb)
                comb.pop()
        
        
        backtrack(0, 0, [])
        return ans
                
                