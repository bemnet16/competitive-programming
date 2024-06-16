class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        
        for ast in asteroids:
            
            while stack and stack[-1] < -ast and stack[-1] > 0 and ast < 0:
                stack.pop()
                
            if not stack:
                stack.append(ast)
                
            elif stack and stack[-1] == -ast and stack[-1] > 0 and ast < 0:
                stack.pop()
            
            elif stack[-1] < 0 or ast > 0:
                stack.append(ast)
        
        
        return stack
            
        