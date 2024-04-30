class Solution:
    def countBits(self, n: int) -> List[int]:
        
        answer = [0]
        
        for i in range(1, (n + 1)):
            
            t = 1
            
            while i > 1:
                
                if i & 1:
                    t += 1
                
                i = i >> 1
            
            answer.append(t)
        
        
        return answer
        