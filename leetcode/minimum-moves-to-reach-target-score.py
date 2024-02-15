class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        answer = 0
        
        while target > 1:
            
            isEven = target % 2 == 0
            
            if isEven and maxDoubles:
                target //= 2
                maxDoubles -= 1
            
            elif maxDoubles == 0:
                answer += (target - 1)
                break
                
            else:
                target -= 1
            
            answer += 1
        
        return answer