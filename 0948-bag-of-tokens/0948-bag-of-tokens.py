class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens.sort()
        
        scores = 0
        
        face_up = 0
        face_down = len(tokens) - 1
        
        for i in range(len(tokens)):
            
            if power >= tokens[face_up]:
                scores += 1
                power -= tokens[face_up]
                face_up += 1
            
            
            elif face_down - face_up >= 2 and scores >= 1:
                scores -= 1
                power += tokens[face_down]
                face_down -= 1
        
        return scores
            
            
            
            
            
            
            
            
            
            
            