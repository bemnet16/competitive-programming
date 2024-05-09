class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        ans = []
        
        def backtrack(permut, idx):
            
            if len(permut) == len(s):
                ans.append("".join(permut))
                return
            
            for i in range(idx, len(s)):
                
                if s[i].isalpha():
                    
                    permut.append(s[i].lower())
                    backtrack(permut, i + 1)
                    permut.pop()
                    
                    permut.append(s[i].upper())
                    backtrack(permut, i + 1)
                    permut.pop()
                    
                else:
                    permut.append(s[i])
                    backtrack(permut, i + 1)
                    permut.pop()
        
        
        
        backtrack([], 0)
        return ans