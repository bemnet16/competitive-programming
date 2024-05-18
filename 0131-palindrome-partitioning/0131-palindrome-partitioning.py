class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        
        answer = []
        temp = []
        
        def isPalindrome(start, end):
            
            while start < end:
                if s[start] != s[end]:
                    return False
                
                start += 1
                end -= 1
                
            return True
        
        
        
        def backtrack(i):
            
            if i >= len(s):
                answer.append(temp.copy())
                return
            
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    temp.append(s[i: j + 1])
                    backtrack(j + 1)
                    temp.pop()
        
        
        backtrack(0)
        return answer