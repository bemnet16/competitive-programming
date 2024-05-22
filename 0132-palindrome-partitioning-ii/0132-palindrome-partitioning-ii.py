class Solution:
    def minCut(self, s: str) -> int:
        ans=[]
       
        def isPalndrom(s):
            return s==s[::-1]
        @cache
        def helper(s):
            if not s:
                return 0
            if isPalndrom(s):
                return 0
            ans=len(s)-1
            for i in range(1,len(s)):
                if isPalndrom(s[:i]):
                    ans=min(ans,1+helper(s[i:]))   
            return ans
        return helper(s)
                
   






        