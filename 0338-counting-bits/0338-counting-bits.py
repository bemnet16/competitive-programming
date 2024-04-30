class Solution:
    def countBits(self, n: int) -> List[int]:
        
        answer = [0]
        
        for i in range(1, (n + 1)):
            
            count = 0
            
            while i > 0:
                
                count += 1
                i = i & (i - 1)
            
            answer.append(count)
        
        
        return answer
        