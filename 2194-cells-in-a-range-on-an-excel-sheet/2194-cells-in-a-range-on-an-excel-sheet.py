class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        
        answer = []
        
        c1, c2 = s[0], s[3]
        r1, r2 = int(s[1]), int(s[4])
        
        for i in range(ord(c1), ord(c2) + 1):
            for j in range(r1, r2 + 1):
                
                answer.append(str(chr(i)) + str(j))
        
        
        return answer
        